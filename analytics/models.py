from django.db import models

# Create your models here.


class Event(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    additional_data = models.TextField(blank=True, default='')
