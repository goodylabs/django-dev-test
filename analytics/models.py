from django.conf import settings
from django.db import models
from django.dispatch import receiver
from . import authentication

# Create your models here.


# Note: authentication-related models are defined in authentication.py.


@receiver(models.signals.post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **_kwargs):
    """Provide tokens to users automatically."""
    print(sender, instance, created)
    if created:
        token = authentication.AnalyticsToken.objects.create(user=instance)
        print(token)
        token.save()


class Event(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    additional_data = models.TextField(blank=True, default='')
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, )
