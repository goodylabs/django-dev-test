from rest_framework import generics
from .serializers import EventSerializer
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from django.contrib.auth.models import User
from rest_framework.exceptions import NotAuthenticated


class EventCreate(generics.CreateAPIView):
    serializer_class = EventSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(created_by=User.objects.get(username=self.request.user))
        else:
            raise NotAuthenticated()
