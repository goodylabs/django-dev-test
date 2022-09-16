from django.conf import settings
from django.db import models
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication

# Custom token-based authentication.


class AnalyticsToken(models.Model):
    key = models.CharField('Key', max_length=100, primary_key=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='api_token',
        on_delete=models.CASCADE, verbose_name='User',
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super().save(*args, **kwargs)

    @property
    def created(self):
        return self.created_at

    @classmethod
    def generate_key(cls):
        return binascii.hexlify(os.urandom(50)).decode()


class AnalyticsTokenAuthentication(TokenAuthentication):
    keyword = 'Bearer'
    model = AnalyticsToken

    def __init__(self, *args, **kwargs):
        super(AnalyticsTokenAuthentication, self).__init__(*args, **kwargs)
