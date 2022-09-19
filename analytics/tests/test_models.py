from django.test import TestCase
from analytics.models import Event
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class EventModelTestCase(TestCase):
    def setUp(self):
        self.correct_user = User.objects.create(username='correctuser', password='Zxcvbnm^123')
        self.correct_event = Event.objects.create(
            name='some_name',
            additional_data='some_text',
            created_by=self.correct_user
        )
        self.token = Token(user=self.correct_user)

    def test_event_creation(self):
        self.assertIsNotNone(self.correct_user.id)
        self.assertIsNotNone(self.correct_event.id)
        self.assertIsNotNone(self.token)
