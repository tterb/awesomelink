from django.core.validators import URLValidator
from django.utils.timesince import timesince
from rest_framework import serializers

from .helpers import flatten_redirects
from .models import AwesomeLink
from .validators import validate_awesomeness


class AwesomeLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = AwesomeLink
        fields = ['id', 'url', 'created', 'updated', 'clicks', 'rating', 'rating_count']

    # pylint: disable=no-self-use
    def validate_url(self, value):
        # Make sure the URL isn't a redirect to another page
        url_validator = URLValidator()
        url_validator(value)
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
