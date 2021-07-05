from django import forms
from django.contrib import admin
from .models import AwesomeLink


class AwesomeLinkAdminForm(forms.ModelForm):
    class Meta:
        model = AwesomeLink
        fields = ['url', 'is_approved']

    def clean_normalized_url(self):
        if not self.cleaned_data['normalized_url']:
            raise forms.ValidationError('An AwesomeLink with this URL already exists')
        return self.cleaned_data['normalized_url']

@admin.register(AwesomeLink)
class AwesomeLinkAdmin(admin.ModelAdmin):
    form = AwesomeLinkAdminForm
