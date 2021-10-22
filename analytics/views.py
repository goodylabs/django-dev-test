import json

from django.contrib.auth.models import User
from rest_framework import permissions, mixins, status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Event
from .serializers import UserSerializer, EventSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class EventApiView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    @action(methods=['POST'], detail=False)
    def post(self, request):
        raw = json.dumps(request.data)
        data = json.loads(raw)
        name = data.get('name')
        additional_data = data.get('additional_data')

        event_data = {
            'name': name,
            'additional_data': additional_data,
        }

        event = Event.objects.create(**event_data)

        data = {
            "message": f"New event created with id: {event.id}"
        }
        serializer = EventSerializer(data=event_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
