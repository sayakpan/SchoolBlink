import os
from datetime import datetime
from typing import Optional
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import DetailView, UpdateView, CreateView, DeleteView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate
from django.urls import reverse
from django.urls import reverse_lazy

from Accounts.models import User
from Parent.models import *
from Profiles.models import *
from Admissions.models import *
from Parent.forms import *


# User Type Test


class ParentTest(UserPassesTestMixin):
    def test_func(self) -> bool | None:
        return self.request.user.is_parent


# Create your views here.


class ParentProfileView(LoginRequiredMixin, ParentTest, DetailView):
    context_object_name = "parent"
    model = ParentProfile
    template_name = "Parent/parentProfile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_classes = SchoolClass.objects.all()
        all_country = Country.objects.all()
        all_state = State.objects.all()
        all_city = City.objects.all()
        parent = context["parent"]
        all_applications = ApplicationForm.objects.filter(parent=parent)
        print(all_applications)
        context["all_classes"] = all_classes
        context["all_country"] = all_country
        context["all_state"] = all_state
        context["all_city"] = all_city
        context["all_applications"] = all_applications
        context["parent_slug"] = self.kwargs.get("slug")
        return context


class AccountUpdateView(LoginRequiredMixin, ParentTest, UpdateView):
    model = ParentProfile
    form_class = AccountUpdateForm
    template_name = "Parent/parentProfile.html"

    def get_success_url(self):
        return reverse("Parent:parentProfile", kwargs={"slug": self.object.slug})

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        user = User.objects.get(email=email)
        user.first_name = form.cleaned_data.get("name")
        user.save()
        return super().form_valid(form)


class PersonalDataUpdateView(LoginRequiredMixin, ParentTest, UpdateView):
    model = ParentProfile
    form_class = PersonalDataUpdateForm
    template_name = "Parent/parentProfile.html"

    def get_success_url(self) -> str:
        return reverse("Parent:parentProfile", kwargs={"slug": self.object.slug})


class UploadProfilePictureView(LoginRequiredMixin, ParentTest, UpdateView):
    model = ParentProfile
    form_class = ProfilePictureForm
    template_name = "Parent/parentProfile.html"

    def get_success_url(self) -> str:
        return reverse("Parent:parentProfile", kwargs={"slug": self.object.slug})

    def form_valid(self, form):
        parent_profile = self.get_object()
        # Delete the old image
        old_image_path = parent_profile.profile_image.path
        if os.path.exists(old_image_path):
            os.remove(old_image_path)
        form.save()
        return super().form_valid(form)


class DeleteChildProfileView(DeleteView):
    model = ChildProfile
    template_name = "Parent/parentProfile.html"

    def get_success_url(self):
        parent_profile_slug = self.object.parent.slug
        return reverse("Parent:parentProfile", kwargs={"slug": parent_profile_slug})


# Function Based Views


def userTypeTest(user):
    return user.is_parent


@user_passes_test(userTypeTest)
@login_required
def ResetPasswordView(request, slug):
    user = request.user
    if request.method == "POST":
        oldPassword = request.POST.get("oldPassword")
        newPassword = request.POST.get("newPassword")
        confirmPassword = request.POST.get("confirmPassword")

        user_valid = authenticate(username=user.username, password=oldPassword)

        if user_valid:
            current_user = User.objects.get(username=user.username)
            if newPassword == oldPassword:
                current_user.set_password(newPassword)
                current_user.save()
        else:
            messages.error(
                request,
                "Wrong password. Try again or click forgot password to reset it",
                extra_tags="reset",
            )
            HttpResponseRedirect(reverse("Parent:parentProfile", kwargs={"slug": slug}))

    return HttpResponseRedirect(reverse("Parent:parentProfile", kwargs={"slug": slug}))


@user_passes_test(userTypeTest)
@login_required
def AddChildProfileView(request, slug):
    user = request.user
    if request.method == "POST":
        child = ChildProfile()
        child.name = request.POST.get("name")
        child.gender = request.POST.get("gender")

        date_of_birth_str = request.POST.get("date_of_birth")
        date_of_birth_obj = datetime.strptime(date_of_birth_str, "%d %b %Y")
        date_of_birth_formatted = date_of_birth_obj.strftime("%Y-%m-%d")
        child.date_of_birth = date_of_birth_formatted

        class_choosen_id = request.POST.get("interested_class")
        child.interested_class = SchoolClass.objects.get(id=class_choosen_id)
        child.parent = ParentProfile.objects.get(user=user)
        child.save()
    return HttpResponseRedirect(reverse("Parent:parentProfile", kwargs={"slug": slug}))


@user_passes_test(userTypeTest)
@login_required
def UpdateChildProfileView(request, slug):
    user = request.user
    if request.method == "POST":
        child_id = request.POST.get("child_id")
        child = ChildProfile.objects.get(id=child_id)
        child.name = request.POST.get("name")

        date_of_birth_str = request.POST.get("date_of_birth")
        date_of_birth_obj = datetime.strptime(date_of_birth_str, "%d %b %Y")
        date_of_birth_formatted = date_of_birth_obj.strftime("%Y-%m-%d")
        child.date_of_birth = date_of_birth_formatted

        class_choosen_id = request.POST.get("interested_class")
        child.interested_class = SchoolClass.objects.get(id=class_choosen_id)
        child.save()
    return HttpResponseRedirect(reverse("Parent:parentProfile", kwargs={"slug": slug}))
