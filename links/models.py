from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.core.validators import URLValidator

from .constants import AWESOMELINK_UNIQUE_ERROR
from .helpers import (
    can_be_embedded,
    flatten_redirects,
    normalize_url,
    upgrade_protocol,
)


class AwesomeLink(models.Model):
    url            = models.URLField(max_length=900, validators=[URLValidator], unique=True)
    normalized_url = models.CharField(max_length=900, unique=True)
    clicks         = models.PositiveIntegerField(default=0)
    created        = models.DateTimeField(editable=False)
    updated        = models.DateTimeField(blank=True)
    rating         = models.FloatField(blank=True, default=0.0)
    rating_count   = models.IntegerField(blank=True, default=0)
    flag_count     = models.PositiveIntegerField(default=0)
    is_embeddable  = models.BooleanField(default=False)
    is_approved    = models.BooleanField(default=False)

    class Meta:
        ordering = ['created']

    def click(self):
        self.clicks += 1
        self.save(update_fields=['clicks'])
        return self.clicks

    def rate(self, new_rating):
        self.rating_count += 1
        self.rating = self.calculate_rating(new_rating)
        self.save(update_fields=['rating', 'rating_count'])
        return self.rating

    def calculate_rating(self, new_rating):
        return ((self.rating * (self.rating_count - 1)) + new_rating) / (self.rating_count)

    def flag(self):
        self.flag_count += 1
        self.save(update_fields=['flag_count'])
        return self.flag_count

    def approve(self):
        self.is_approved = True
        self.save(update_fields=['is_approved'])

    def clean(self):
        qs = self._meta.model.objects.exclude(pk=self.pk)
        qs = qs.filter(normalized_url=self.normalized_url)
        if qs.exists():
            raise ValidationError(AWESOMELINK_UNIQUE_ERROR)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.url, _ =  flatten_redirects(self.url)
            self.url = upgrade_protocol(self.url)
            self.created = timezone.now()
            self.normalized_url = normalize_url(self.url)
            self.is_embeddable = can_be_embedded(self.url)
        self.updated = timezone.now()
        return super(AwesomeLink, self).save(*args, **kwargs)

    def __str__(self):
        return self.url
