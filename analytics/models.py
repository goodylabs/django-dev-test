from django.db import models
from django.utils import timezone

from analytics.validators import LessThanNowValidator


class Event(models.Model):
    """
       Stores information about the event.
    """
    name = models.CharField('the name of the event', max_length=255)
    created_at = models.DateTimeField(default=timezone.now, validators=[LessThanNowValidator()])
    additional_data = models.CharField(max_length=300, blank=True, default='')

    class Meta:
        verbose_name = "event"
        verbose_name_plural = "events"

    def __str__(self):
        return f"{self.name}"
