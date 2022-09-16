from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from rest_framework.authtoken.models import TokenProxy
from . import authentication, models

# Register your models here.


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', )
    search_fields = ('name', 'created_by__username', )


# Remove the detault, unused auth tokens from the panel.
admin.site.unregister(TokenProxy)


# Add the adequate auth tokens.
@admin.register(authentication.AnalyticsToken)
class AnalyticsTokenAdmin(admin.ModelAdmin):
    list_display = ('user', 'key', )


# Add column to the users list.
UserAdmin.list_display += ('api_token_url', )


def api_token_url(_user_admin, obj):
    """Render clickable api token for the users list."""
    key = obj.api_token.key
    return format_html(
        f'<a href="/admin/analytics/analyticstoken/{key}">{key}</a>')


UserAdmin.api_token_url = api_token_url
