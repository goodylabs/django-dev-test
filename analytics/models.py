from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    additional_data = models.TextField(blank=True, default='')
