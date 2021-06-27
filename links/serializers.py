from django.contrib.auth import get_user_model
from django.core.validators import URLValidator
from django.utils.timesince import timesince
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .helpers import flatten_redirects
from .models import AwesomeLink
from .validators import validate_awesomeness


class AwesomeLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = AwesomeLink
        fields = ['pk', 'url', 'created', 'updated', 'clicks', 'rating', 'rating_count', 'is_approved']
    
    def validate_url(self, value):
        # Make sure the URL isn't a redirect to another page
        URLValidator()(value)
        value = flatten_redirects(value)
        validate_awesomeness(value)
        return value

    def to_representation(self, instance):
        """
        Format AwesomeLink attributes in response
        """
        repr = super().to_representation(instance)
        repr['created'] = timesince(instance.created)
        repr['updated'] = timesince(instance.updated)
        return repr


class AwesomeLinkListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AwesomeLink
        fields = ['url']