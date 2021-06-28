import random
import requests
from urllib.parse import urlparse, ParseResult

from .constants import (
    MAX_REDIRECT_COUNT,
    CLIENT_ERROR_CODE_MIN,
    SERVER_ERROR_CODE_MAX,
)


def get_random_link(awesome_links):
    """
    Get a random AwesomeLink
    """
    return random.choice(awesome_links)

def check_link_status(awesome_link):
    """
    Check for a dead AwesomeLink
    """
    response = requests.get(awesome_link.url)
    return CLIENT_ERROR_CODE_MIN < response.status_code < SERVER_ERROR_CODE_MAX

def flatten_redirects(url):
    """
    Flattens shortened links or redirects and return the destination URL
    """
    current = url
    prev = ''
    redirect_count = 0
    try:
        while bool(current != prev):
            # Limit the amount of redirects or we could be here all day
            if redirect_count > MAX_REDIRECT_COUNT:
                raise Exception('Maximum redirection limit exceeded')
            prev = current
            current = requests.get(prev).url
            redirect_count += 1
        return current
    except Exception as url_error:
        raise Exception(f'Unable to open {url}') from url_error

def normalize_url(url):
    """
    Normalize URLs to improve duplicate detection
    """
    try:
        parsed_url = urlparse(url)
        # Strip the protocol, index.html, and trailing slashes
        return ParseResult('', *parsed_url[1:]).geturl().strip('index.html').strip('/')
    except Exception as parse_error:
        raise Exception(f'Unable to normalize {url}') from parse_error

def can_be_embedded(url):
    """
    Detect headers that prevent a page from being embedded in an iframe
    """
    response = requests.get(url)
    headers = response.headers
    if 'X-Frame-Options' in headers and \
        (headers['X-Frame-Options'] == 'SAMEORIGIN' or \
        headers['X-Frame-Options'] == 'DENY' or \
        headers['X-Frame-Options'] == 'ALLOW-FROM'):
        return False
    return True
