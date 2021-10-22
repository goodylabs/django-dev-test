from django.test import TestCase

from .models import Event


class EventTestCase(TestCase):
    def test_post(self):
        self.assertEquals(
            Event.objects.count(),
            0
        )
        Event.objects.create(
            name='event1',
        )
        Event.objects.create(
            name='event2', additional_data="datatataczydata",
        )
        self.assertEquals(
            Event.objects.count(),
            2
        )
