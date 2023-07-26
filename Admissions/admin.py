from django.contrib import admin
from Admissions.models import *

# Register your models here.


@admin.register(AdmissionOpenClasses)
class AdmissionOpenClassesAdmin(admin.ModelAdmin):
    raw_id_fields = ("school",)
    list_display = ["id", "school", "class_opened", "status"]


@admin.register(ApplicationForm)
class ApplicationFormAdmin(admin.ModelAdmin):
    raw_id_fields = (
        "parent",
        "child",
        "school",
    )
    list_display = ["id", "parent", "child", "school", "submitted_for_class", "is_paid"]
