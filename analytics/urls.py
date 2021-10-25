from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import EventApiView

router = DefaultRouter()
router.register(r'events', EventApiView)

urlpatterns = [
    path(r'', include(router.urls)),
]
