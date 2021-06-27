import random, requests
from urllib.parse import urlparse, ParseResult
from urllib.request import urlopen
from django.core.exceptions import ValidationError

from .constants import MAX_REDIRECT_COUNT


def get_random_link(awesome_links):
    return random.choice(awesome_links)

# Flattens shortened links or redirects and return the destination URL
def flatten_redirects(url):
    current = url
    prev = ''
    redirect_count = 0
    try:
        while bool(current != prev):
            # Limit the amount of redirects or we could be here all day
            if redirect_count > MAX_REDIRECT_COUNT:
                raise Exception(f'Maximum redirection limit exceeded')
            prev = current
            current = requests.get(prev).url
            redirect_count += 1
        return current
    except:
        raise Exception(f'Unable to open {url}')

# Normalize URLs to improve detect duplicates
def normalize_url(url):
    try:
        parsed_url = urlparse(url)
        # Strip the protocol, index.html, and trailing slashes
        return ParseResult('', *parsed_url[1:]).geturl().strip('index.html').strip('/')
    except:
        raise Exception(f'Unable to normalize {url}')
