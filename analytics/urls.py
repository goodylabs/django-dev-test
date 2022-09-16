from django.urls import include, path
from rest_framework import routers
from . import views

# Register your URL configuration here.


router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
urlpatterns = [
    path('', views.home, name='home'),
    path('api', include(router.urls)),
    path('api/events', views.event_list),
]
