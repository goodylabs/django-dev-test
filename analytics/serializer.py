from rest_framework import serializers
from . import models
from .models import User


class EventSerializer(serializers.ModelSerializer):

    name = serializers.CharField(max_length=255)
    additional_data = serializers.CharField()
    # created_by = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = models.Event
        fields = '__all__'
