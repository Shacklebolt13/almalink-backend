from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as _UserAdmin

from .models import User


@admin.register(User)
class UserAdmin(_UserAdmin):
    list_display = ("email", "first_name", "last_name", "is_staff")
    search_fields = ("email", "first_name", "last_name")

    ordering = ("email",)

    list_per_page = 50
