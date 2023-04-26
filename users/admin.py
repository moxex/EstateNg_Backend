from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from .models import Profile
User = get_user_model()


class UserAdmin(BaseUserAdmin):
    list_display = [
        "id",
        "email",
        "username",
        "is_staff",
        "is_active",
    ]

class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        "seller",
        "agency_name",
    ]

admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)

 