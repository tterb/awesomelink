import json
import mock
from django.db.models import DateTimeField
from django.forms.models import model_to_dict
from django.http import HttpRequest
from django.test import TestCase
from django.urls import reverse
from django.utils.timesince import timesince
from rest_framework import status

from links.constants import (
    VISITED_LINKS_COOKIE,
)
from links.models import AwesomeLink
from links.helpers import (
    get_visited_links,
    update_visited_links,
)
from links.views import (
    awesomelink_view
)
from .constants import VALID_URLS


class AwesomeLinkHelperTest(TestCase):
    """ Test module for AwesomeLink helpers """

    def setUp(self):
        self.links = []
        self.unapproved_links = []
        self.approved_links = []
        # Create five test urls
        for index, url in enumerate(VALID_URLS):
            link = AwesomeLink.objects.create(url=url)
            self.links.append(link)
            if index % 2:
                # Approve only the even indices
                link.approve()
                self.approved_links.append(link)
            else:
                self.unapproved_links.append(link)

    def test_get_visited_links(self):
        request = HttpRequest()
        # Should correctly parse valid cookie data
        request.COOKIES[VISITED_LINKS_COOKIE] = '1,2,3,4,5'
        self.assertEqual([1,2,3,4,5], get_visited_links(request))

    def test_get_visited_links_invalid(self):
        request = HttpRequest()
        # Should return an empty array on invalid data
        request.COOKIES[VISITED_LINKS_COOKIE] = 'hello world'
        self.assertEqual([], get_visited_links(request))

    def test_update_visited_links(self):
        # Should insert the new ID at the front of the list and the result should be stringified
        visited = list(range(2, 21))
        newID = 1
        expectedResult = ','.join(map(str, list(range(1, 21))))
        self.assertEqual(expectedResult, update_visited_links(visited, newID))
        # Should insert the new ID to the front and the last should be removed because the max-length is 20
        visited = list(range(1, 21))
        newID = 0
        expectedResult = ','.join(map(str, list(range(0, 20))))
        self.assertEqual(expectedResult, update_visited_links(visited, newID))

    def test_update_visited_links_empty(self):
        # If visited is empty, should return just the stringified ID
        visited = []
        newID = 20
        self.assertEqual(str(newID), update_visited_links(visited, newID))

