from django.contrib.auth.models import User
from django.http import JsonResponse
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


class EventApiView( mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    @action(methods=['POST'], detail=False)
    def post(self, request):
        tutorial_serializer = EventSerializer(data=request.data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return Response(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return Response(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['GET'], detail=False)
    def get_all_events(self, request):
        events = Event.objects.all()
        events_serializer = EventSerializer(events, many=True)
        return JsonResponse(events_serializer.data, safe=False)
