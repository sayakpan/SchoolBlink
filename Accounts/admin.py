from django.contrib import admin
from Accounts.models import User
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm


# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = [
        "username",
        "first_name",
        "is_active",
        "User_Type",
        "is_staff",
        "is_superuser",
        "date_joined",
    ]
    ordering = ["-date_joined"]

    def User_Type(self, obj):
        if obj.is_school and obj.is_parent:
            return "School and Parent"
        elif obj.is_school:
            return "School"
        elif obj.is_parent:
            return "Parent"
        else:
            return ""

    fieldsets = (
        (
            "User Profile",
            {"fields": ("is_school", "is_parent", "username", "password")},
        ),
        ("Personal info", {"fields": ("first_name", "last_name", "email")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    form = CustomUserChangeForm


admin.site.register(User, CustomUserAdmin)
