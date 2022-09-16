from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

# Create your middleware here.


class AnalyticsTokenAuthMiddleware(MiddlewareMixin):
    # Simple authentication middleware that can be extended later.

    def __init__(self, get_response, **kwargs):
        super().__init__(self, **kwargs)
        self.get_response = get_response

    def __call__(self, request):
        """Modern middleware call."""
        user = request.user
        if user.is_authenticated:
            return self.get_response(request)
        return HttpResponse('Unauthorised', status=401)

    def process_view(
            self, request, _view_func, *_view_args, **_view_kwargs):
        """MiddlewareMixin-compatible middleware call."""
        return self(request)
