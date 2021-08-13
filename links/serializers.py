from django.core.serializers.json import Serializer
from django.db.models import DateTimeField
from django.utils.timesince import timesince

from .models import AwesomeLink


class AwesomeLinkListSerializer(Serializer):

    excluded_fields = {'normalized_url', 'flag_count', 'is_embeddable', 'is_approved', 'is_secure'}

    def get_dump_object(self, obj):
        model_fields = AwesomeLink._meta.fields
        for field in model_fields:
            if field.name in self.excluded_fields:
                # Remove excluded model-fields
                del self._current[field.name]
            elif field.__class__ == DateTimeField:
                # Format DateTimeFields
                self._current[field.name] = getattr(obj, field.name).strftime('%m/%d/%Y')
            else:
                self._current[field.name] = getattr(obj, field.name)
        return self._current

class AwesomeLinkSerializer:

    excluded_fields = {'normalized_url', 'flag_count', 'is_embeddable', 'is_approved', 'is_secure'}

    def __init__(self, awesomelink, attach=[], exclude=[]):
        self.excluded_fields.update(exclude)
        # Remove 'attach' values from excluded fields
        self.excluded_fields.difference_update(attach)
        self.data = dict()
        model_fields = awesomelink._meta.fields
        for field in model_fields:
            if field.__class__ == DateTimeField:
                # Format DateTimeFields
                self.data[field.name] = timesince(getattr(awesomelink, field.name))
            elif field.name not in self.excluded_fields:
                # Add model-fields that aren't excluded
                self.data[field.name] = getattr(awesomelink, field.name)
