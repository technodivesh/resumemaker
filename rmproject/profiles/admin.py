from django.contrib import admin

from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('guid', 'full_name', 'email', 'is_active', 'created_at', 'updated_at')
    search_fields = ('full_name', 'email')

# Register your models here.
