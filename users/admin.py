from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as _UserAdmin

from .models import User


@admin.register(User)
class UserAdmin(_UserAdmin):
    list_display = ("username", "email", "first_name", "last_name", "is_staff")
    search_fields = ("username", "email", "first_name", "last_name")

    ordering = (
        "username",
        "email",
    )

    list_per_page = 50
