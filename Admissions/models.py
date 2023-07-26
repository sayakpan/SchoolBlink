from django.db import models
from Accounts.models import *
from Parent.models import *
from Profiles.models import *

# Create your models here.


class AdmissionOpenClasses(models.Model):
    school = models.ForeignKey(
        School_Profiles, on_delete=models.DO_NOTHING, related_name="school_profiles"
    )
    class_opened = models.ForeignKey(SchoolClass, on_delete=models.DO_NOTHING)
    form_limit = models.IntegerField(blank=True, null=True)
    form_price = models.IntegerField(blank=True, null=True)
    status = models.CharField(
        max_length=10,
        choices=(("1", "Open"), ("0", "Closed")),
        default="0",
        blank=True,
        null=True,
    )

    def __str__(self):
        return str(self.class_opened) + " - " + str(self.school)

    class Meta:
        verbose_name_plural = "Admission Open Classes"


class ApplicationForm(models.Model):
    parent = models.ForeignKey(
        ParentProfile, on_delete=models.DO_NOTHING, related_name="application_form"
    )
    child = models.ForeignKey(ChildProfile, on_delete=models.DO_NOTHING)
    school = models.ForeignKey(
        School_Profiles,
        on_delete=models.DO_NOTHING,
        related_name="applications_received",
        blank=True,
    )
    submitted_for_class = models.ForeignKey(
        AdmissionOpenClasses, on_delete=models.DO_NOTHING
    )

    # Application Fields
    parent_name = models.CharField(max_length=20, blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    blood_group = models.CharField(max_length=10, blank=True, null=True)
    mother_toungh = models.CharField(max_length=20, blank=True, null=True)
    religion = models.CharField(max_length=20, blank=True, null=True)
    category = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)

    is_paid = models.BooleanField(default=False, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.parent_name = self.parent.name
        self.name = self.child.name
        self.gender = self.child.gender
        self.date_of_birth = self.child.date_of_birth
        self.mobile = self.parent.phone_number
        self.school = self.submitted_for_class.school
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.id) + " " + str(self.parent) + " " + str(self.name)

    class Meta:
        verbose_name_plural = "Application Form"
