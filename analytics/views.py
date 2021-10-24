from django.contrib.auth.models import User
from django.http import JsonResponse, QueryDict
from rest_framework import permissions, mixins, status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Event, CustomUser
from .serializers import UserSerializer, EventSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class EventApiView(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    API endpoint that allows events to be viewed or added.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    @action(methods=['POST'], detail=False)
    def post(self, request):

        try:
            r_token = request.META['Authorization']
        except KeyError:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        api_token = r_token.replace('Bearer ', '')

        custom_user = CustomUser.objects.filter(api_token=api_token).first()
        if custom_user:
            data_updated = QueryDict.copy(request.data)
            data_updated['created_by'] = custom_user.id

            tutorial_serializer = EventSerializer(data=data_updated)
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                return Response(tutorial_serializer.data, status=status.HTTP_201_CREATED)
            return Response(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    @action(methods=['GET'], detail=False)
    def get_all_events(self, request):
        events = Event.objects.all()
        events_serializer = EventSerializer(events, many=True)
        return JsonResponse(events_serializer.data, safe=False)
