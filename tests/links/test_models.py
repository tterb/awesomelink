# from django.core.exceptions import ValidationError
import requests, requests_mock
from django.db import transaction
from django.db.utils import IntegrityError
from django.test import TestCase
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from links.helpers import can_be_embedded
from links.models import AwesomeLink
from links.serializers import AwesomeLinkSerializer
from links.validators import validate_awesomeness
from .constants import (
    BLACKLISTED_URLS,
    FRAMEABLE_HEADERS, 
    NON_FRAMEABLE_HEADERS,
)


class AwesomeLinkModelTest(TestCase):
    """ Test module for AwesomeLink model """

    def setUp(self):
        self.awesome_link = AwesomeLink.objects.create(url='https://joyoftesting.com/hidden-valley/')

    def test_invalid_url(self):
        invalid_urls = [
            'This is invalid',
            'this.is.invalid',
            123,
            True,
        ]
        for url in invalid_urls:
            serializer = AwesomeLinkSerializer(data={'url': url})
            self.assertFalse(serializer.is_valid())
            # with self.assertRaises(ValidationError):
            #     with transaction.atomic():
            #         AwesomeLink.objects.create(url=url)
    
    def test_blacklisted_urls(self):
        for url in BLACKLISTED_URLS:
            serializer = AwesomeLinkSerializer(data={'url': url})
            # self.assertFalse(serializer.is_valid())
            with self.subTest(url=url):
                with self.assertRaises(ValidationError):
                    with transaction.atomic():
                        validate_awesomeness(url)


    def test_normalized_url(self):
        self.assertEqual(self.awesome_link.normalized_url, 'joyoftesting.com/hidden-valley')

    def test_unique_urls(self):
        unique_urls = [
            'https://joyoftesting.com/alaskan-waterfall/',
            'https://joyoftesting.com/hidden-valley/?page=2',
            'https://joyoftesting.com/hidden-valley/base.html',
        ]
        for url in unique_urls:
            try:
               link = AwesomeLink.objects.create(url=url)
            except:
               self.fail(f'Failed to create AwesomeLink: {url}')

    def test_duplicate_urls(self):
        # Test that duplicate URLs are caught by normalization
        duplicate_urls = [
            'https://joyoftesting.com/hidden-valley/',
            'https://joyoftesting.com/hidden-valley',
            'http://joyoftesting.com/hidden-valley',
            'https://joyoftesting.com/hidden-valley/index.html',
        ]
        for url in duplicate_urls:
            with self.assertRaises(IntegrityError):
                with transaction.atomic():
                    AwesomeLink.objects.create(url=url)

    def test_rating(self):
        self.awesome_link.rate(4)
        self.assertEqual(self.awesome_link.rating, 4.0)
        self.assertEqual(self.awesome_link.rating_count, 1)
        self.awesome_link.rate(3)
        self.assertEqual(self.awesome_link.rating, 3.5)
        self.assertEqual(self.awesome_link.rating_count, 2)
        self.awesome_link.rate(2)
        self.assertEqual(self.awesome_link.rating, 3.0)
        self.assertEqual(self.awesome_link.rating_count, 3)

    def test_click(self):
        # Clicks should initially be 0
        self.assertEqual(self.awesome_link.clicks, 0)
        self.awesome_link.click()
        self.assertEqual(self.awesome_link.clicks, 1)

    @requests_mock.Mocker()
    def test_is_embeddable(self, mock):
        # Mock request to return frameable headers
        mock.get('https://joyoftesting.com/hidden-valley/', headers=FRAMEABLE_HEADERS)
        self.assertTrue(can_be_embedded(self.awesome_link.url))
        # Mock request to return headers that prevent embedding
        mock.get('https://joyoftesting.com/hidden-valley/', headers=NON_FRAMEABLE_HEADERS)
        self.assertFalse(can_be_embedded(self.awesome_link.url))


    def test_approval(self):
        # Approval should initially be false by default
        self.assertFalse(self.awesome_link.is_approved)
        self.awesome_link.approve()
        self.assertTrue(self.awesome_link.is_approved)

        

