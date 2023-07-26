from django.db import models
from django.utils.text import slugify
from Accounts.models import User
from Profiles.models import *

# Create your models here.


class ParentProfile(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="parent_profiles"
    )
    name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    slug = models.SlugField(max_length=255, blank=True, null=True)

    profile_image = models.ImageField(
        upload_to="profile_images",
        default="static/images/profile_image_default.jpg",
        null=True,
        blank=True,
    )

    gender = models.CharField(
        max_length=10,
        choices=(
            ("M", "Male"),
            ("F", "Female"),
            ("U", "Prefer Not to Say"),
        ),
        blank=True,
        null=True,
    )

    qualification = models.CharField(
        max_length=50,
        choices=(
            ("No", "No Formal Education"),
            ("12", "Class 12 or below"),
            ("Graduate", "Graduate"),
            ("Post Graduate", "Post Graduate"),
            ("Doctorate", "Doctorate"),
        ),
        blank=True,
        null=True,
    )

    relation_with_child = models.CharField(
        max_length=50,
        choices=(
            ("Father", "Father"),
            ("Mother", "Mother"),
            ("Guardian", "Guardian"),
        ),
        null=True,
        blank=True,
    )

    income_range = models.CharField(
        max_length=50,
        choices=(
            ("70000", "Below 70,000"),
            ("140000", "70,000 to 1.4 Lakhs"),
            ("240000", "1.4 Lakhs to 2.4 Lakhs"),
            ("800000", "2.4 Lakhs to 8 Lakhs"),
            ("1500000", "8 Lakhs to 15 Lakhs"),
            ("3000000", "15 Lakhs to 30 Lakhs"),
            ("15000000", "30 Lakhs to 1.5 Crores"),
            ("99999999", "Above 1.5 Crores"),
        ),
        null=True,
        blank=True,
    )

    interested_class = models.ForeignKey(
        SchoolClass,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )

    city = models.ForeignKey(City, on_delete=models.DO_NOTHING, null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.DO_NOTHING, null=True, blank=True)
    country = models.ForeignKey(
        Country, on_delete=models.DO_NOTHING, null=True, blank=True
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            unique_id = 1
            while ParentProfile.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{unique_id}"
                unique_id += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.name)

    @property
    def gender_choices(self):
        return self._meta.get_field("gender").choices

    @property
    def qualification_choices(self):
        return self._meta.get_field("qualification").choices

    @property
    def relation_with_child_choices(self):
        return self._meta.get_field("relation_with_child").choices

    @property
    def income_range_choices(self):
        return self._meta.get_field("income_range").choices

    class Meta:
        verbose_name_plural = "Parent Profile"


class ChildProfile(models.Model):
    parent = models.ForeignKey(
        ParentProfile,
        on_delete=models.CASCADE,
        related_name="child",
        blank=True,
        null=True,
    )
    name = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(auto_now_add=False, blank=True, null=True)
    gender = models.CharField(
        max_length=10, choices=(("Boy", "Boy"), ("Girl", "Girl")), blank=True, null=True
    )
    interested_class = models.ForeignKey(
        SchoolClass,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = "Child Profile"
