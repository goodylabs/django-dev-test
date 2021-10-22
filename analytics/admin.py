from django.contrib import admin

from analytics.models import (
    Event,
    CustomUser,
)

admin.site.register(CustomUser)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    search_fields = ['name']
