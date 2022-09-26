import binascii
import os
from django.conf import settings
from django.db import models, utils, transaction
from rest_framework.authentication import TokenAuthentication

import random

# Custom token-based authentication.


class AnalyticsToken(models.Model):
    # Reimplementation of Token with longer keys.

    key = models.CharField('Key', max_length=100, primary_key=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='api_token',
        on_delete=models.CASCADE, verbose_name='User',
    )
    # It is ``created_at'' instead of ``created'' for the consistency with
    # the listed tasks and event model.
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        try:
            with transaction.atomic():
                return super().save(*args, **kwargs)
        except utils.IntegrityError:
            self.key = None
            return self.save(*args, **kwargs)

    @property
    def created(self):
        """Alias added for Token compatibility."""
        return self.created_at

    @classmethod
    def generate_key(cls):
        """Generate 100 characters long key."""
        return binascii.hexlify(os.urandom(50)).decode()


class AnalyticsTokenAuthentication(TokenAuthentication):
    # Subclass of TokenAuthentication with custom keyword and token model.
    keyword = 'Bearer'
    model = AnalyticsToken
