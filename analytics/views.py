# from django.shortcuts import render
from django.utils.decorators import decorator_from_middleware, method_decorator
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import middleware, models, serializers

# Create your views here.


analytics_token_protected = decorator_from_middleware(
    middleware.AnalyticsTokenAuthMiddleware)


@api_view(['GET'])
def home(_request):
    """Render the most basic home page ever designed."""
    return Response('Analytics app seems to be running.')


class EventList(generics.ListCreateAPIView):
    # /events/api endpoint.

    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer

    @method_decorator(analytics_token_protected)
    def list(self, _request, *_args, **_kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    @method_decorator(analytics_token_protected)
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
