from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm
from django.utils.safestring import mark_safe
from django.contrib.auth.forms import ReadOnlyPasswordHashField


custom_user_model = get_user_model()


class CustomUserChangeForm(UserChangeForm):
    password = ReadOnlyPasswordHashField(
        label=("Password"),
        help_text=mark_safe(
            "Raw passwords are not stored, so there is no way to see "
            "this user's password, but you can change the password "
            'using <a href="../password/">this form</a>.'
        ),
    )
