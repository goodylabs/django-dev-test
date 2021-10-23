from django.contrib.auth.models import User
from rest_framework import serializers

from analytics.models import Event


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class EventSerializer(serializers.ModelSerializer):
    """Event serializer."""

    class Meta:
        model = Event
        fields = '__all__'
