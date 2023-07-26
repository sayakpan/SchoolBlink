from django import forms
from Profiles.models import *
from Admissions.models import *


class AddSchoolForm(forms.ModelForm):
    class Meta:
        model = School_Profiles
        exclude = ["user"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            self.add_error(None, "Email already exists.")
        return email


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("password", "email")


class ParentSignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("first_name", "email", "password")


class SchoolDetailsUpdateForm(forms.ModelForm):
    class Meta:
        model = School_Profiles
        fields = (
            "school_name",
            "email",
            "number",
            "website",
            "address",
            "school_timings",
            "year_established",
            "coed_status",
            "school_medium",
            "ownership",
            "about",
            "school_format",
            "school_type",
            "school_board",
            "school_class",
            "city",
            "state",
            "country",
        )


class LogoForm(forms.ModelForm):
    logo = forms.ImageField()

    class Meta:
        model = School_Profiles
        fields = ["logo"]


class AvailableClassForm(forms.ModelForm):
    class Meta:
        model = School_Profiles
        fields = ["school_class"]


class AdmissionOpenClassesForm(forms.ModelForm):
    class Meta:
        model = AdmissionOpenClasses
        fields = ["form_limit", "form_price", "status", "class_opened", "school"]


class SchoolFacilitiesForm(forms.ModelForm):
    class Meta:
        model = SchoolFacilities
        fields = "__all__"
