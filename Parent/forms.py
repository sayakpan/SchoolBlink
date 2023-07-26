from django import forms
from Parent.models import *
from Admissions.models import *


class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = ParentProfile
        fields = ("name", "email", "phone_number")


class PersonalDataUpdateForm(forms.ModelForm):
    class Meta:
        model = ParentProfile
        fields = (
            "date_of_birth",
            "gender",
            "qualification",
            "relation_with_child",
            "income_range",
            "interested_class",
            "city",
            "state",
            "country",
        )


class ProfilePictureForm(forms.ModelForm):
    profile_image = forms.ImageField()

    class Meta:
        model = ParentProfile
        fields = ["profile_image"]


class UpdateChildProfileForm(forms.ModelForm):
    class Meta:
        model = ChildProfile
        fields = (
            "name",
            "date_of_birth",
            "gender",
            "interested_class",
        )
