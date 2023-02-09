import re
import requests
from django import forms
from django.core.validators import URLValidator

from .constants import (
    BLACKLIST_DOMAINS,
    BLACKLIST_URL_ERROR,
    DEFAULT_REQUEST_TIMEOUT,
    URL_INVALID_ERROR,
)


def validate_url(url):
    try:
        url_validator = URLValidator(schemes=['http', 'https'])
        url_validator(url)
        requests.get(url, timeout=DEFAULT_REQUEST_TIMEOUT)
    except Exception as url_error:
        raise forms.ValidationError(
            URL_INVALID_ERROR,
            params={'url':url},
            code=400
        ) from url_error

def validate_awesomeness(url):
    """
    Check URL for blacklisted domains
    """
    for domain in BLACKLIST_DOMAINS:
        if re.match(domain['pattern'], url):
            raise forms.ValidationError(
                BLACKLIST_URL_ERROR,
                params={'domain':domain['name']},
                code=400
            )
