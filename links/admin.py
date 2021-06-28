from django.contrib import admin
from .models import AwesomeLink


class AwesomeLinkModelAdmin(admin.ModelAdmin):
    # exclude = ('rating', 'rating_count', 'slug', 'updated')
    class Meta:
        model = AwesomeLink

    def get_readonly_fields(self, request, obj=None):
        fields = []
        if obj:
            fields += [
                'created',
                'updated',
                'normalized_url',
                'clicks',
                'rating',
                'rating_count',
                'flag_count',
                'is_embeddable'
            ]
        return fields

admin.site.register(AwesomeLink, AwesomeLinkModelAdmin)
