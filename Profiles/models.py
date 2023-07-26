from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from Accounts.models import User


# Create your models here.
class Country(models.Model):
    id = models.AutoField(primary_key=True, unique=True, editable=False)
    country_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.country_name


class State(models.Model):
    id = models.AutoField(primary_key=True, unique=True, editable=False)
    state_name = models.CharField(max_length=50, unique=True)
    country_id = models.ForeignKey(Country, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.state_name


class City(models.Model):
    id = models.AutoField(primary_key=True, unique=True, editable=False)
    city_name = models.CharField(max_length=50, unique=True)
    state_id = models.ForeignKey(State, on_delete=models.DO_NOTHING)
    country_id = models.ForeignKey(Country, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.city_name


class SchoolType(models.Model):
    school_type = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.school_type)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.school_type)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "School Type"


class SchoolFormat(models.Model):
    school_format = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.school_format)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.school_format)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "School Format"


class SchoolBoard(models.Model):
    school_board = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.school_board)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.school_board)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "School Board"
        ordering = ["school_board"]


class SchoolClass(models.Model):
    rank = models.IntegerField(blank=True, null=True)
    school_class = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return str(self.school_class)

    class Meta:
        verbose_name_plural = "School Class"
        ordering = ["rank"]


class School_Profiles(models.Model):
    id = models.AutoField(primary_key=True, unique=True, editable=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="school_profiles", unique=False
    )
    school_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    website = models.URLField(max_length=200, null=True, blank=True)
    number = models.CharField(max_length=15)
    slug = models.SlugField(max_length=255, blank=True)
    address = models.CharField(max_length=400)

    school_format = models.ForeignKey(
        SchoolFormat, on_delete=models.DO_NOTHING, blank=True, null=True
    )
    school_type = models.ForeignKey(
        SchoolType, on_delete=models.DO_NOTHING, blank=True, null=True
    )
    school_board = models.ManyToManyField(SchoolBoard, blank=True)
    school_class = models.ManyToManyField(SchoolClass, blank=True)
    school_timings = models.CharField(max_length=200, blank=True, null=True)
    year_established = models.CharField(max_length=10, blank=True, null=True)

    latitude = models.CharField(
        max_length=200, default="22.960301417322228", blank=True, null=True
    )
    longitude = models.CharField(
        max_length=200, default="79.56199782489124", blank=True, null=True
    )

    coed_status = models.CharField(
        max_length=10,
        choices=(
            ("1", "Co-ed"),
            ("2", "Boys"),
            ("3", "Girls"),
        ),
        blank=True,
        null=True,
    )
    school_medium = models.CharField(
        max_length=10,
        choices=(
            ("1", "English"),
            ("2", "Bengali"),
            ("3", "Hindi"),
        ),
        blank=True,
        null=True,
    )
    ownership = models.CharField(
        max_length=10,
        choices=(
            ("1", "Private"),
            ("2", "Government"),
        ),
        blank=True,
        null=True,
    )

    logo = models.ImageField(
        upload_to="school_logos",
        default="static\images\school_default_2.png",
        null=True,
    )
    cover = models.ImageField(
        upload_to="school_covers",
        default="static\images\school_default_cover1.jpg",
        null=True,
    )

    about = models.TextField(max_length=20000, blank=True, null=True)

    is_featured = models.BooleanField(default=False)

    city = models.ForeignKey(
        City, on_delete=models.DO_NOTHING, related_name="school_profiles"
    )
    state = models.ForeignKey(
        State, on_delete=models.DO_NOTHING, related_name="school_profiles"
    )
    country = models.ForeignKey(
        Country, on_delete=models.DO_NOTHING, related_name="school_profiles"
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.school_name)
            slug = base_slug
            unique_id = 1
            while School_Profiles.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{unique_id}"
                unique_id += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.school_name

    @property
    def coed_status_choices(self):
        return self._meta.get_field("coed_status").choices

    @property
    def school_medium_choices(self):
        return self._meta.get_field("school_medium").choices

    @property
    def ownership_choices(self):
        return self._meta.get_field("ownership").choices

    class Meta:
        verbose_name = "School Profile"
        verbose_name_plural = "School Profiles"


class SchoolFacilities(models.Model):
    CHOICE = (("Y", "YES"), ("N", "NO"), ("U", "Unknown"))

    school = models.ForeignKey(
        School_Profiles, on_delete=models.CASCADE, related_name="facilities"
    )

    AC_Classes = models.CharField(max_length=10, choices=CHOICE, default="U")
    Wifi = models.CharField(max_length=10, choices=CHOICE, default="U")
    Smart_Classes = models.CharField(max_length=10, choices=CHOICE, default="U")
    Boys_Hostel = models.CharField(max_length=10, choices=CHOICE, default="U")
    Girls_Hostel = models.CharField(max_length=10, choices=CHOICE, default="U")
    Cafeteria = models.CharField(max_length=10, choices=CHOICE, default="U")
    Library = models.CharField(max_length=10, choices=CHOICE, default="U")
    Playground = models.CharField(max_length=10, choices=CHOICE, default="U")
    Auditorium = models.CharField(max_length=10, choices=CHOICE, default="U")
    CCTV = models.CharField(max_length=10, choices=CHOICE, default="U")
    GPS_Bus_Tracking_App = models.CharField(max_length=10, choices=CHOICE, default="U")
    Student_Tracking_App = models.CharField(max_length=10, choices=CHOICE, default="U")
    Alumni_Association = models.CharField(max_length=10, choices=CHOICE, default="U")
    Medical_Room = models.CharField(max_length=10, choices=CHOICE, default="U")
    Day_care = models.CharField(max_length=10, choices=CHOICE, default="U")
    Meals = models.CharField(max_length=10, choices=CHOICE, default="U")
    Transportation = models.CharField(max_length=10, choices=CHOICE, default="U")
    Art_and_Craft = models.CharField(max_length=10, choices=CHOICE, default="U")
    Dance = models.CharField(max_length=10, choices=CHOICE, default="U")
    Drama = models.CharField(max_length=10, choices=CHOICE, default="U")
    Music = models.CharField(max_length=10, choices=CHOICE, default="U")
    Picnics_and_excursion = models.CharField(max_length=10, choices=CHOICE, default="U")
    Debate = models.CharField(max_length=10, choices=CHOICE, default="U")
    Gardening = models.CharField(max_length=10, choices=CHOICE, default="U")
    Indoor_Sports = models.CharField(max_length=10, choices=CHOICE, default="U")
    Outdoor_Sports = models.CharField(max_length=10, choices=CHOICE, default="U")
    Karate = models.CharField(max_length=10, choices=CHOICE, default="U")
    Taekwondo = models.CharField(max_length=10, choices=CHOICE, default="U")
    Yoga = models.CharField(max_length=10, choices=CHOICE, default="U")
    Gym = models.CharField(max_length=10, choices=CHOICE, default="U")
    Swimming_Pool = models.CharField(max_length=10, choices=CHOICE, default="U")
    Skating = models.CharField(max_length=10, choices=CHOICE, default="U")
    Horse_Riding = models.CharField(max_length=10, choices=CHOICE, default="U")
    Computer_Lab = models.CharField(max_length=10, choices=CHOICE, default="U")
    Science_Lab = models.CharField(max_length=10, choices=CHOICE, default="U")
    Robotics_Lab = models.CharField(max_length=10, choices=CHOICE, default="U")
    Ramps = models.CharField(max_length=10, choices=CHOICE, default="U")
    Washrooms = models.CharField(max_length=10, choices=CHOICE, default="U")
    Elevators = models.CharField(max_length=10, choices=CHOICE, default="U")

    def __str__(self):
        return str(self.school)

    class Meta:
        verbose_name_plural = "School Facilities"


@receiver(post_save, sender=School_Profiles)
def create_school_facilities(sender, instance, created, **kwargs):
    if created:
        SchoolFacilities.objects.create(school=instance)
