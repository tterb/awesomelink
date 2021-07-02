import json, mock, pytest
from django.forms.models import model_to_dict
from django.test import TestCase
from django.urls import reverse
from django.utils.timesince import timesince
from rest_framework import status

from links.models import AwesomeLink
from links.views import (
    awesomelink_list,
    awesomelink_count,
    awesomelink_detail,
    awesomelink_rate,
    awesomelink_specific,
    awesomelink_submit,
    awesomelink_view
)
from .constants import VALID_URLS


class AwesomeLinkModelTest(TestCase):
# class TestAwesomeLinkViews:
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
        # request_url = reverse(awesomelink_list)
        expected_data = [{ 'url': link.url } for link in self.approved_links]
        response = self.client.get('/list')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)

    def test_awesomelink_count(self):
        request_url = reverse(awesomelink_count)
        response = self.client.get(request_url)
        # View returns a JSONResponse
        data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data['count'], len(self.approved_links))

    @mock.patch('links.helpers.is_link_alive')
    def test_awesomelink_view(self, mock_is_link_alive):
        # mocker.patch('links.helpers.is_link_alive', return_value=True)
        # @patch('links.helpers.is_link_alive', True)
        mock_is_link_alive.return_value = True
        # Set all awesomelinks as embeddable
        for link in self.approved_links:
            link.is_embeddable = True
            link.save(update_fields=['is_embeddable'])
        request_url = reverse(awesomelink_view)
        response = self.client.get(reverse(awesomelink_view))
        # Should load the link framed in the page
        self.assertEqual(response.status_code, 200)

        # Set all awesomelinks as not embeddable
        for link in self.approved_links:
            link.is_embeddable = False
            link.save(update_fields=['is_embeddable'])
        request_url = reverse(awesomelink_view)
        response = self.client.get(reverse(awesomelink_view))
        # Should redirect to the url
        self.assertEqual(response.status_code, 302)


    def test_awesomelink_detail(self):
        awesomelink = self.approved_links[0]
        request_url = reverse(awesomelink_detail, kwargs={'pk':awesomelink.pk})
        response = self.client.get(request_url)
        # View returns a JSONResponse
        data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Get model fields as a dictionary
        fields_dict = model_to_dict(awesomelink)
        # Because the serializer processes the DateTimeFields using timesince
        fields_dict['created'] = timesince(awesomelink.created)
        fields_dict['updated'] = timesince(awesomelink.created)
        hidden_fields = {'normalized_url', 'flag_count', 'is_approved', 'is_embeddable'}
        # Ensure that the correct fields are returned from the serializer
        for key in fields_dict.keys():
            if key in hidden_fields:
                self.assertFalse(key in data)
            else:
                self.assertEqual(data[key], fields_dict[key])

    def test_awesomelink_specific(self):
        approved_url = reverse(awesomelink_specific, kwargs={'pk':self.approved_links[0].pk})
        unapproved_url = reverse(awesomelink_specific, kwargs={'pk':self.unapproved_links[0].pk})
        # View should redirect if the link is approved
        response = self.client.get(approved_url)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        # View should return a 404 if the link isn't approved
        response = self.client.get(unapproved_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_awesomelink_rate(self):
        requestData = {
            'pk': self.approved_links[0].pk,
            'rating': 4.0,
        }
        response = self.client.post(reverse(awesomelink_rate), requestData)
        # View returns a JSONResponse
        data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data['rating'], 4.0)
        self.assertEqual(data['rating_count'], 1)

    def test_awesomelink_submit(self):
        submittedUrl = 'https://example.com/'
        requestData = {
            'url': submittedUrl,
        }
        response = self.client.post(reverse(awesomelink_submit), requestData)
        # View returns a JSONResponse
        data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(data['url'], submittedUrl)
        # There should be a matching AwesomeLink
        links = AwesomeLink.objects.filter(url=submittedUrl)
        self.assertEqual(links.count(), 1)
        # Submitted links should not be approved
        self.assertFalse(links[0].is_approved)
