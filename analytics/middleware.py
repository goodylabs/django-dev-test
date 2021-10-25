"""Module containing middleware implementations."""

from django.utils.deprecation import MiddlewareMixin

from .models import CustomUser


class CustomHeaderMiddleware(MiddlewareMixin):

    def process_request(self, request):
        user_id = request.POST.get('created_by', False)
        try:
            api_token = CustomUser.objects.get(user=user_id).api_token
        except CustomUser.DoesNotExist:
            api_token = ''
        request.META['Authorization'] = "Bearer " + api_token
        response = self.get_response(request)
        return response
