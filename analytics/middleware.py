"""Module containing middleware implementations."""

from .models import CustomUser


class MyMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user_id = request.POST.get('created_by', False)
        try:
            api_token = CustomUser.objects.get(user=user_id).api_token

        except CustomUser.DoesNotExist:
            api_token = ''
        response = self.get_response(request)
        response['Authorization'] = "Bearer " + api_token
        return response
