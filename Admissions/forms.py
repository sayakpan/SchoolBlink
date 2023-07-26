from django import forms
from Admissions.models import *


class SchoolApplicationForm(forms.ModelForm):
    class Meta:
        model = ApplicationForm
        fields = "__all__"


class PaymentForm(forms.ModelForm):
    class Meta:
        model = ApplicationForm
        fields = [
            "is_paid",
        ]
