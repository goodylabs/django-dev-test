from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
import datetime


class Event(models.Model):
    name = models.CharField(max_length=255,  blank=False, default=None)
    created_at = models.DateTimeField(default=datetime.datetime.now)
    additional_data = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

