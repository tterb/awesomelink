from urllib.parse import urlparse, ParseResult
from django.db import models
from django.utils import timezone
from django.utils.timesince import timesince
from django.core.validators import URLValidator

from .helpers import normalize_url, flatten_redirects
# from .validators import validate_awesomeness


class AwesomeLink(models.Model):
    url            = models.URLField(max_length=900, validators=[URLValidator], unique=True)
    normalized_url = models.CharField(max_length=900, unique=True)
    clicks         = models.PositiveIntegerField(default=0)
    created        = models.DateTimeField(editable=False)
    updated        = models.DateTimeField(blank=True)
    rating         = models.FloatField(blank=True, default=0.0)
    rating_count   = models.IntegerField(blank=True, default=0)
    flag_count     = models.PositiveIntegerField(default=0)
    is_approved     = models.BooleanField(default=False)

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
        return (self.rating * self.rating_count + new_rating) / (self.rating_count)

    def flag(self):
        self.flag_count += 1
        self.save(update_fields=['flag_count'])
        return self.flag_count

    def approve(self):
        self.is_approved = True
        self.save(update_fields=['is_approved'])


    def save(self, *args, **kwargs):
        # Only set timestamp on create
        if not self.pk:
            # self.clean()
            self.url =  flatten_redirects(self.url)
            self.created = timezone.now()
            self.normalized_url = normalize_url(self.url)
        self.updated = timezone.now()
        return super(AwesomeLink, self).save(*args, **kwargs)

    def __str__(self):
        return self.url
