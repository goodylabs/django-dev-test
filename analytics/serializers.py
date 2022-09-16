from rest_framework import serializers
from . import models

# Create your serializers here.


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Event
        fields = ['name', 'created_at', 'additional_data']
