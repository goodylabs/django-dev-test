from django.contrib import admin

from analytics.models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    search_fields = ['name']
