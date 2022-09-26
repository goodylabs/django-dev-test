from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from rest_framework import exceptions
from . import authentication

# Create your middleware here.


class AnalyticsTokenAuthMiddleware(MiddlewareMixin):
    # Simple authentication middleware that can be extended later.

    def __init__(self, get_response, **kwargs):
        super().__init__(self, **kwargs)
        self.get_response = get_response

    def __call__(self, request):
        """Modern middleware call."""
        auth_result = None
        try:
            auth_result = (
                authentication.AnalyticsTokenAuthentication().authenticate(
                    request))
        except exceptions.AuthenticationFailed:
            pass
        if auth_result:
            return self.get_response(request)
        return HttpResponse('Unauthorised', status=401)
