import re
from django.utils.http import url_has_allowed_host_and_scheme
from rest_framework import serializers

from .constants import BLACKLIST_DOMAINS


def validate_safe_link(url):
    return url_has_allowed_host_and_scheme(
        url,
        allowed_hosts=None,
        require_https=False
    )

def validate_awesomeness(url):
    """
    Check URL for blacklisted domains
    """
    # blacklist_pattern = '|'.join([domain['pattern'] for domain in BLACKLIST_DOMAINS])
    for domain in BLACKLIST_DOMAINS:
        # if re.match(blacklist_pattern, url):
        if re.match(domain['pattern'], url):
            # raise serializers.ValidationError(f'That link is not very awesome')
            raise serializers.ValidationError(f'{domain["name"]} links are not very awesome')
