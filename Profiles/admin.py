from django.contrib import admin
from Profiles.models import *
from import_export.admin import ImportExportModelAdmin, ImportExportMixin
from import_export import resources, fields


class SchoolProfileImportResource(resources.ModelResource):
    class Meta:
        model = School_Profiles
        exclude = ("slug",)


class SchoolProfileExportResource(resources.ModelResource):
    city = fields.Field(attribute="city")
    state = fields.Field(attribute="state")
    country = fields.Field(attribute="country")

    def export_city(self, school_profiles):
        return school_profiles.city.city_name

    def export_state(self, school_profiles):
        return school_profiles.state.state_name

    def export_country(self, school_profiles):
        return school_profiles.country.country_name

    class Meta:
        model = School_Profiles
        fields = (
            "id",
            "school_name",
            "email",
            "number",
            "address",
            "city",
            "state",
            "country",
        )
        export_order = (
            "id",
            "school_name",
            "email",
            "number",
            "address",
            "city",
            "state",
            "country",
        )


@admin.register(School_Profiles)
class School_Profiles_Admin(ImportExportModelAdmin):
    raw_id_fields = ("user", "city", "state", "country")
    filter_horizontal = ("school_class", "school_board")
    list_display = (
        "id",
        "school_name",
        "user",
        "email",
        "number",
        "address",
        "city",
        "state",
        "country",
    )

    # Import Fields
    resource_class = SchoolProfileImportResource

    # Export Fields
    def get_export_resource_class(self):
        return SchoolProfileExportResource

    def city(self, obj):
        return obj.city.city_name

    def state(self, obj):
        return obj.state.state_name

    def country(self, obj):
        return obj.country.country_name


@admin.register(Country)
class Country_Admin(admin.ModelAdmin):
    list_display = ["id", "country_name"]


@admin.register(State)
class State_Admin(admin.ModelAdmin):
    raw_id_fields = ("country_id",)
    list_display = ["id", "state_name", "country_id"]

    def country(self, obj):
        return obj.country_id.country_name


@admin.register(City)
class City_Admin(admin.ModelAdmin):
    raw_id_fields = ("country_id", "state_id")
    list_display = ["id", "city_name", "state_id", "country_id"]

    def state(self, obj):
        return obj.state_id.state_name

    def country(self, obj):
        return obj.country_id.country_name


@admin.register(SchoolFormat)
class SchoolFormat_Admin(admin.ModelAdmin):
    list_display = ["id", "school_format", "slug"]


@admin.register(SchoolType)
class SchoolType_Admin(admin.ModelAdmin):
    list_display = ["id", "school_type", "slug"]


@admin.register(SchoolBoard)
class SchoolBoard_Admin(admin.ModelAdmin):
    list_display = ["id", "school_board", "slug"]


@admin.register(SchoolClass)
class SchoolClass_Admin(admin.ModelAdmin):
    list_display = ["id", "rank", "school_class"]


class SchoolFacilitiesImportResource(resources.ModelResource):
    class Meta:
        model = SchoolFacilities

    @property
    def import_id_fields(self):
        # Exclude 'id' from import_id_fields
        return [field for field in super().import_id_fields if field != "id"]


class SchoolFacilitiesExportResource(resources.ModelResource):
    school = fields.Field(attribute="school")

    class Meta:
        model = SchoolFacilities
        fields = [
            "school",
            "AC_Classes",
            "Wifi",
            "Smart_Classes",
            "Boys_Hostel",
            "Girls_Hostel",
            "Cafeteria",
            "Library",
            "Playground",
            "Auditorium",
            "CCTV",
            "GPS_Bus_Tracking_App",
            "Student_Tracking_App",
            "Alumni_Association",
            "Medical_Room",
            "Day_care",
            "Meals",
            "Transportation",
            "Art_and_Craft",
            "Dance",
            "Drama",
            "Music",
            "Picnics_and_excursion",
            "Debate",
            "Gardening",
            "Indoor_Sports",
            "Outdoor_Sports",
            "Karate",
            "Taekwondo",
            "Yoga",
            "Gym",
            "Swimming_Pool",
            "Skating",
            "Horse_Riding",
            "Computer_Lab",
            "Science_Lab",
            "Robotics_Lab",
            "Ramps",
            "Washrooms",
            "Elevators",
        ]

    def dehydrate_school(self, school_facilities):
        # Customize the export value for the 'school' field
        return school_facilities.school.id


@admin.register(SchoolFacilities)
class SchoolFacilitiesAdmin(ImportExportModelAdmin):
    raw_id_fields = ("school",)
    list_display = [
        "id",
        "school",
    ]

    # Import Fields
    resource_class = SchoolFacilitiesImportResource

    # Export Fields
    def get_export_resource_class(self):
        return SchoolFacilitiesExportResource
