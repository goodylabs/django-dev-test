import django.core.exceptions
from django.contrib import auth
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from . import models

# Create your tests here.


class EventModelTests(TestCase):
    # Event model tests.

    @classmethod
    def setUpTestData(cls):
        cls.user = auth.get_user_model().objects.create(username='EMT1UName')
        cls.user.save()
        for create_kwargs in [
                {'name': 'EMT1Name', 'created_by': cls.user},
                {
                    'name': 'EMT2Name',
                    'created_by': cls.user,
                    'additional_data': 'EMT1Ad'},
                {
                    'name': 'EMT3Name',
                    'created_by': cls.user,
                    'additional_data': 'x' * 257},
                {
                    'name': 'EMT4Name_' + 'x' * (255 - len('EMT4Name_')),
                    'created_by': cls.user}, ]:
            event = models.Event.objects.create(**create_kwargs)
            event.save()
            event.full_clean()

    def test_names(self):
        """Test names of the created entities."""
        self.assertEqual(models.Event.objects.get(id=1).name, 'EMT1Name')
        self.assertEqual(models.Event.objects.get(id=2).name, 'EMT2Name')
        self.assertEqual(models.Event.objects.get(id=3).name, 'EMT3Name')
        event4 = models.Event.objects.get(id=4)
        self.assertTrue(event4.name.startswith('EMT4Name_'))
        self.assertTrue(len(event4.name) == 255)

    def test_additional_data(self):
        """Test additional_data of the created entities."""
        self.assertEqual(models.Event.objects.get(id=1).additional_data, '')
        self.assertIsNotNone(models.Event.objects.get(id=2).additional_data)
        self.assertTrue(
            len(models.Event.objects.get(id=3).additional_data) > 256)

    def test_max_length(self):
        """Attempt to create event with overly long name."""
        validation_error = False
        event = models.Event.objects.create(
            name='x' * 256, created_by=self.user)
        try:
            event.full_clean()
        except django.core.exceptions.ValidationError:
            validation_error = True
        self.assertTrue(validation_error)


class EventAPIViewTests(TestCase):
    # Event API view tests.

    @classmethod
    def setUpTestData(cls):
        cls.user = auth.get_user_model().objects.create(username='EMT1UName')
        cls.user.save()

    def test_url_exists(self):
        """Check '/api/events/ URL."""
        response = self.client.get('/api/events')
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)
        authorized_client = APIClient()
        authorized_client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.user.api_token.key}')
        ac_response = authorized_client.get('/api/events')
        self.assertEqual(status.HTTP_200_OK, ac_response.status_code)


class EventAPISerializerTests(APITestCase):
    # Event API/serializer tests.

    @classmethod
    def setUpTestData(cls):
        cls.user = auth.get_user_model().objects.create(username='EMT1UName')
        cls.user.save()

    def test_post(self):
        """Attemt to post minimal piece of data to '/api/events' endpoint."""
        response = self.client.post('/api/events', {
            'name': 'EST1Name', })
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)
        authorized_client = APIClient()
        authorized_client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.user.api_token.key}')
        ac_response = authorized_client.post('/api/events', {
            'name': 'EST1Name', })
        self.assertEqual(status.HTTP_201_CREATED, ac_response.status_code)


class AnalyticsTokenModelTests(TestCase):
    # AnalyticsToken model tests.

    @classmethod
    def setUpTestData(cls):
        cls.user = django.contrib.auth.get_user_model().objects.create(
            username='ATMT1Uname')
        cls.user.save()

    def test_token(self):
        """Test the new user for api_token presence and length."""
        self.assertIsNotNone(self.user.api_token)
        self.assertEqual(len(self.user.api_token.key), 100)
