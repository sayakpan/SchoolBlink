from django.contrib import admin
from Parent.models import *


# Register your models here.
@admin.register(ParentProfile)
class ParentProfileAdmin(admin.ModelAdmin):
    raw_id_fields = ("user", "city", "state", "country")
    list_display = ["id", "name", "email", "phone_number"]


@admin.register(ChildProfile)
class ChildProfileAdmin(admin.ModelAdmin):
    raw_id_fields = ("parent",)
    list_display = [
        "id",
        "name",
        "parent",
        "gender",
        "date_of_birth",
        "interested_class",
    ]
