import factory
from django.contrib.auth.models import User
from django.test import TestCase

from .models import Event


class UserFactory(factory.django.DjangoModelFactory):
    """Factory of users."""

    class Meta:
        model = User

    username = factory.Sequence(lambda n: "User %d" % n)


class EventFactory(factory.django.DjangoModelFactory):
    """Factory of events."""

    class Meta:
        model = Event

    created_by = None

    class Params:
        event = factory.Trait(
            created_by=factory.SubFactory(UserFactory)
        )


class EventTestCase(TestCase):

    def test_post(self):
        self.assertEquals(
            Event.objects.count(),
            0
        )
        EventFactory.create(event=True)
        self.assertEquals(
            Event.objects.count(),
            1
        )

        EventFactory.create(event=True)
        EventFactory.create(event=True)
        EventFactory.create(event=True)
        EventFactory.create(event=True)
        self.assertEquals(
            Event.objects.count(),
            5
        )
