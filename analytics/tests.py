import django.core.exceptions
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from . import models

# Create your tests here.


class EventModelTests(TestCase):
    # Event model tests.

    @classmethod
    def setUpTestData(cls):
        for create_kwargs in [
                {'name': 'EMT1Name', },
                {'name': 'EMT2Name', 'additional_data': 'EMT1Ad'},
                {'name': 'EMT3Name', 'additional_data': 'x' * 257},
                {'name': 'EMT4Name_' + 'x' * (255 - len('EMT4Name_'))}, ]:
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
        event = models.Event.objects.create(name='x' * 256)
        try:
            event.full_clean()
        except django.core.exceptions.ValidationError:
            validation_error = True
        self.assertTrue(validation_error)


class EventAPIViewTests(TestCase):
    # Event API view tests.

    def test_url_exists(self):
        """Check '/api/events/ URL."""
        response = self.client.get('/api/events')
        self.assertEqual(response.status_code, 200)


class EventAPISerializerTests(APITestCase):
    # Event API/serializer tests.

    def test_post(self):
        """Attemt to post minimal piece of data to '/api/events' endpoint."""
        response = self.client.post('/api/events', {
            'name': 'EST1Name', })
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
