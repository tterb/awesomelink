import json
import mock
from django.db.models import DateTimeField
from django.forms.models import model_to_dict
from django.test import TestCase
from django.urls import reverse
from django.utils.timesince import timesince
from rest_framework import status

from links.constants import (
    AWESOMELINK_DNE_ERROR,
    AWESOMELINK_UNAPPROVED_ERROR,
    AWESOMELINK_UNIQUE_ERROR,
    INVALID_RATING_ERROR,
)
from links.models import AwesomeLink
from links.views import (
    awesomelink_list,
    awesomelink_count,
    awesomelink_detail,
    awesomelink_flag,
    awesomelink_rate,
    awesomelink_specific,
    awesomelink_submit,
    awesomelink_view
)
from .constants import VALID_URLS


class AwesomeLinkViewsTest(TestCase):
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
        request_url = reverse(awesomelink_list)
        # Get expected response data
        expected_data = dict()
        expected_data['count'] = len(self.approved_links)
        expected_data['links'] = []
        excluded_fields = {'normalized_url', 'flag_count', 'is_approved', 'is_embeddable'}
        for link in self.approved_links:
            expected_link = dict()
            for field in AwesomeLink._meta.fields:
                if field.__class__ == DateTimeField:
                    expected_link[field.name] = getattr(link, field.name).strftime('%m/%d/%Y')
                elif field.name not in excluded_fields:
                    expected_link[field.name] = getattr(link, field.name)
            expected_data['links'].append(expected_link)

        response = self.client.get(request_url)
        data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, expected_data)

    def test_awesomelink_count(self):
        request_url = reverse(awesomelink_count)
        response = self.client.get(request_url)
        # View returns a JSONResponse
        data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data['count'], len(self.approved_links))

    @mock.patch('links.helpers.is_alive')
    def test_awesomelink_view_embed(self, mock_is_alive):
        mock_is_alive.return_value = True
        request_url = reverse(awesomelink_view)
        # Set all awesomelinks as embeddable
        for link in self.approved_links:
            link.is_embeddable = True
            link.save(update_fields=['is_embeddable'])
        request_url = reverse(awesomelink_view)
        response = self.client.get(request_url)
        # Should load the link framed in the page
        self.assertEqual(response.status_code, 200)

    @mock.patch('links.helpers.is_alive')
    def test_awesomelink_view_redirect(self, mock_is_alive):
        mock_is_alive.return_value = True
        request_url = reverse(awesomelink_view)
        # Set all awesomelinks as not embeddable
        for link in self.approved_links:
            link.is_embeddable = False
            link.save(update_fields=['is_embeddable'])
        response = self.client.get(request_url)
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
        excluded_fields = {'normalized_url', 'flag_count'}
        # Ensure that the correct fields are returned from the serializer
        for key in fields_dict:
            if key in excluded_fields:
                self.assertFalse(key in data)
            else:
                self.assertEqual(data[key], fields_dict[key])

    def test_awesomelink_detail_invalid(self):
        invalid_pk = self.links[-1].pk + 1
        self.assertFalse(invalid_pk in {link.pk for link in self.links})
        request_url = reverse(awesomelink_detail, kwargs={'pk':invalid_pk})
        response = self.client.get(request_url)
        # View returns a JSONResponse
        data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(data['error'], AWESOMELINK_DNE_ERROR)

    def test_awesomelink_specific(self):
        request_url = reverse(awesomelink_specific, kwargs={'pk':self.approved_links[0].pk})
        # View should redirect if the link is approved
        response = self.client.get(request_url)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_awesomelink_unapproved(self):
        request_url = reverse(awesomelink_specific, kwargs={'pk':self.unapproved_links[0].pk})
        # View should return a 404 if the link isn't approved
        response = self.client.get(request_url)
        data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(data['error'], AWESOMELINK_UNAPPROVED_ERROR)

    def test_awesomelink_specific_invalid(self):
        invalid_pk = self.links[-1].pk + 1
        self.assertFalse(invalid_pk in {link.pk for link in self.links})
        request_url = reverse(awesomelink_specific, kwargs={'pk':invalid_pk})
        # Should return an error for invalid pk's
        response = self.client.get(request_url)
        data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(data['error'], AWESOMELINK_DNE_ERROR)

    def test_awesomelink_rate(self):
        request_url = reverse(awesomelink_rate)
        request_data = {
            'pk': self.approved_links[0].pk,
            'rating': 4.0,
        }
        response = self.client.post(request_url, request_data)
        # View returns a JSONResponse
        data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data['rating'], 4.0)
        self.assertEqual(data['rating_count'], 1)

    def test_awesomelink_rate_invalid(self):
        request_url = reverse(awesomelink_rate)
        request_data = {
            'pk': self.approved_links[0].pk,
            'rating': 0.0,
        }
        response = self.client.post(request_url, request_data)
        # View returns a JSONResponse
        data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(data['error'], INVALID_RATING_ERROR)

    def test_awesomelink_flag(self):
        awesomelink = self.approved_links[0]
        initial_count = self.approved_links[0].flag_count
        request_url = reverse(awesomelink_flag)
        request_data = {'pk':awesomelink.pk}
        response = self.client.post(request_url, request_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(awesomelink.flag_count, initial_count)

    def test_awesomelink_submit(self):
        submitted_url = 'https://example.com/'
        request_data = { 'url': submitted_url }
        response = self.client.post(reverse(awesomelink_submit), request_data)
        # View returns a JSONResponse
        data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(data['url'], submitted_url)
        # There should be a matching AwesomeLink
        links = AwesomeLink.objects.filter(url=submitted_url)
        self.assertEqual(links.count(), 1)
        # Submitted links should not be approved
        self.assertFalse(links[0].is_approved)

    def test_awesomelink_submit_duplicate(self):
        # Submit a duplicate URL
        request_data = { 'url': VALID_URLS[0] }
        response = self.client.post(reverse(awesomelink_submit), request_data)
        # View returns a JSONResponse
        data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(data['error'], AWESOMELINK_UNIQUE_ERROR)

    def test_awesomelink_submit_invalid(self):
        # Submit an invalid URL
        invalid_url = 'this.is.invalid'
        request_data = { 'url': invalid_url }
        response = self.client.post(reverse(awesomelink_submit), request_data)
        # View returns a JSONResponse
        data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(data['error'], f'\'http://{invalid_url}\' is not a valid URL')
