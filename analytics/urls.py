from django.urls import path, include
from .views import EventViews
from rest_framework.authtoken import views

urlpatterns = [
    path('events/', EventViews.as_view()),
    path('api-token-auth/', views.obtain_auth_token)
]