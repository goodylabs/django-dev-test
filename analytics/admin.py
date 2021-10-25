from django.contrib import admin
from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'additional_data', 'created_by')
    search_fields = ['name', 'created_by__username']


admin.site.register(Event, EventAdmin)