import json
from django.core.exceptions import ValidationError
from django.db import transaction
from django.db.utils import IntegrityError
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory

from links.models import AwesomeLink
# from links.serializers import AwesomeLinkSerializer
from .constants import VALID_URLS


class AwesomeLinkModelTest(TestCase):
    """ Test module for AwesomeLink views """

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

    def test_awesomelink_list(self):
        expected_data = [{ 'url': link.url } for link in self.approved_links]
        response = self.client.get('/list')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)
    
    def test_awesomelink_detail(self):
        response = self.client.get('/detail/2')
        # View returns a JSONResponse
        responseData = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(responseData['pk'], 2)
        self.assertEqual(responseData['url'], self.links[1].url)
        self.assertTrue(responseData['is_approved'])
        self.assertEqual(responseData['clicks'], 0)
        self.assertTrue('created' in responseData)
        self.assertTrue('updated' in responseData)
        self.assertFalse('normalized_url' in responseData)
        self.assertFalse('flags' in responseData)

    def test_awesomelink_specific(self):
        unapproved_link = f'/{self.unapproved_links[0].pk}'
        approved_link = f'/{self.approved_links[0].pk}'
        # View should return a 404 if the link isn't approved
        response = self.client.get(unapproved_link)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        # View should redirect if the link is approved
        response = self.client.get(approved_link)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_awesomelink_count(self):
        response = self.client.get('/count')
        # View returns a JSONResponse
        responseData = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(responseData['count'], len(self.approved_links))

    def test_awesomelink_rate(self):
        requestData = {
            'pk': self.approved_links[0].pk,
            'rating': 4.0,
        }
        response = self.client.post('/rate', requestData)
        # View returns a JSONResponse
        responseData = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(responseData['rating'], 4.0)
        self.assertEqual(responseData['rating_count'], 1)

