from django.urls import path
from .views import EventCreate

app_name = 'analytics'

urlpatterns = [
    path('api/events', EventCreate.as_view(), name='event_create'),
]
