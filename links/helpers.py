import random
import requests
from urllib.parse import urlparse, ParseResult

from .constants import (
    MAX_REDIRECT_COUNT,
    CLIENT_ERROR_CODE_MIN,
    SERVER_ERROR_CODE_MAX,
    VISITED_LINKS_COOKIE,
)


def get_random_link(awesomelinks):
    """
    Get a random AwesomeLink
    """
    link = random.choice(awesomelinks)
    # Entropy management
    while not is_alive(link.url):
        link = random.choice(awesomelinks)
    return link

def is_error_code(code):
    """
    Return whether the status-code is within the range of a client/server error
    """
    return CLIENT_ERROR_CODE_MIN <= code <= SERVER_ERROR_CODE_MAX

def is_alive(url):
    """
    Check for a dead AwesomeLink
    """
    response = requests.get(url)
    return not is_error_code(response.status_code)

def flatten_redirects(url):
    """
    Flattens shortened links or redirects and return the destination URL and redirect count
    """
    current = url
    prev = ''
    redirect_count = 0
    try:
        while bool(current != prev):
            # Limit the amount of redirects or we could be here all day
            if redirect_count > MAX_REDIRECT_COUNT:
                break
            prev = current
            current = requests.get(prev).url
            redirect_count += 1
        return (current, redirect_count)
    except Exception as url_error:
        raise Exception(f'Unable to open \'{url}\'') from url_error

def normalize_url(url):
    """
    Normalize URLs to improve duplicate detection
    """
    try:
        parsed_url = urlparse(url)
        # Strip the protocol, index.html, and trailing slashes
        return ParseResult('', *parsed_url[1:]).geturl().strip('index.html').strip('/')
    except Exception as parse_error:
        raise Exception(f'Unable to normalize \'{url}\'') from parse_error

def can_be_embedded(url):
    """
    Detect headers that prevent a page from being embedded in an iframe
    """
    response = requests.get(url)
    headers = response.headers
    if 'X-Frame-Options' in headers and \
        (headers['X-Frame-Options'].upper() == 'SAMEORIGIN' or \
        headers['X-Frame-Options'].upper() == 'DENY' or \
        headers['X-Frame-Options'].upper() == 'ALLOW-FROM'):
        return False
    return True

def upgrade_protocol(url):
    """
    Attempt to upgrade the URL protocol from HTTP to HTTPS
    """
    parsed_url = urlparse(url)
    if parsed_url.scheme == 'http':
        upgraded_url = parsed_url._replace(scheme='https').geturl()
        try:
            response = requests.get(upgraded_url)
            if not is_error_code(response.status_code):
                return upgraded_url
        except:
            return url
    return url

def get_visited_links(request):
    """
    Retrieves the viewed link ID's from the user cookies and converts the string to a list of integers
    """
    data = request.COOKIES.get(VISITED_LINKS_COOKIE)
    try:
        return list(map(int, data.split(',')))
    except:
        # If we aren't able to parse the cookie data, than we reset it to an empty list
        return list()

def update_visited_links(visited, id):
    """
    Updates the queue of visited awesomelink ID's with the new ID and returns a stringified queue of at most 20 ID's.
    """
    if not len(visited):
        return str(id)
    # Append new ID to the front
    visited.insert(0, id)
    if len(visited) > 20:
        visited.pop()
    return ','.join(map(str, visited))
