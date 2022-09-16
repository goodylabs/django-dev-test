# from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models, serializers

# Create your views here.


@api_view(['GET'])
def home(_request):
    """Render the most basic home page ever designed."""
    return Response('Analytics app seems to be running.')


@api_view(['GET', 'POST'])
def event_list(request):
    """List all events or create a new event."""
    if request.method == 'GET':
        events = models.Event.objects.all()
        serializer = serializers.EventSerializer(events, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = serializers.EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
