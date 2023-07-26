import os
from typing import Any, Dict, Optional
from django.db import models
from django.forms.models import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import (
    DetailView,
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
)

# Model Imports
from Profiles.models import *
from Parent.models import *
from Admissions.models import *

# Form Imports
from Profiles import forms

# Create your views here.

# MIXIN


class SchoolTest(UserPassesTestMixin):
    def test_func(self) -> bool | None:
        return self.request.user.is_school


# Class Based Views


class ParentSignUpView(CreateView):
    model = User
    template_name = "Profiles/base.html"
    form_class = forms.ParentSignUpForm
    success_url = reverse_lazy("Profiles:index")

    def form_valid(self, form):
        print("in the form")
        name = form.cleaned_data.get("first_name")
        password1 = form.cleaned_data.get("password")
        entered_email = form.cleaned_data.get("email")

        username = User.objects.filter(username=entered_email).exists()

        if username:
            form.add_error("email", "This email is already in use.")
            return self.form_invalid(form)

        form.instance.username = entered_email
        form.instance.set_password(password1)
        form.instance.is_parent = True
        form.instance.save()

        parent = ParentProfile()
        parent.user = form.instance
        parent.name = name
        parent.email = entered_email
        parent.save()

        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, "This email is already in use.", extra_tags="signup"
        )
        return redirect(self.success_url)


class Explore(TemplateView):
    template_name = "Profiles/explore.html"
    http_method_names = ["get", "post"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["school_data"] = School_Profiles.objects.all()
        context["country_data"] = Country.objects.all()
        context["state_data"] = State.objects.all()
        context["city_data"] = City.objects.all()
        context["school_format_data"] = SchoolFormat.objects.all()
        context["school_type_data"] = SchoolType.objects.all()
        context["school_board_data"] = SchoolBoard.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        selected_country_id = request.POST.get("country")
        selected_state_id = request.POST.get("state")
        selected_city_id = request.POST.get("city")
        selected_format_id = request.POST.get("school_format")
        selected_type_id = request.POST.get("school_type")
        selected_board_id = request.POST.get("school_board")

        isfiltered = True
        school_data = School_Profiles.objects.all()

        if selected_country_id and selected_country_id != "-1":
            school_data = school_data.filter(country=selected_country_id)

        if selected_state_id and selected_state_id != "-1":
            school_data = school_data.filter(state=selected_state_id)

        if selected_city_id and selected_city_id != "-1":
            school_data = school_data.filter(city=selected_city_id)

        if selected_format_id and selected_format_id != "-1":
            school_data = school_data.filter(school_format_id=selected_format_id)

        if selected_type_id and selected_type_id != "-1":
            school_data = school_data.filter(school_type_id=selected_type_id)

        if selected_board_id and selected_board_id != "-1":
            school_data = school_data.filter(school_board__id=selected_board_id)

        context = self.get_context_data()
        context["school_data"] = school_data
        context["isfiltered"] = isfiltered
        return render(request, self.template_name, context)


class CustomExplore(TemplateView):
    template_name = "Profiles/explore.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get("slug")
        selected_format = get_object_or_404(SchoolFormat, slug=slug)

        context["school_data"] = School_Profiles.objects.filter(
            school_format=selected_format
        )
        context["country_data"] = Country.objects.all()
        context["state_data"] = State.objects.all()
        context["city_data"] = City.objects.all()
        context["school_format_data"] = SchoolFormat.objects.all()
        context["school_type_data"] = SchoolType.objects.all()
        context["school_board_data"] = SchoolBoard.objects.all()
        return context


class ProfileView(DetailView):
    context_object_name = "school"
    model = School_Profiles
    template_name = "Profiles/profilePage.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get("slug")
        school = School_Profiles.objects.get(slug=slug)
        admission_open_classes = AdmissionOpenClasses.objects.filter(
            school=school
        ).order_by("class_opened")
        context["admission_open_classes"] = admission_open_classes
        return context


class SchoolSettingsView(LoginRequiredMixin, SchoolTest, DetailView):
    context_object_name = "school"
    model = School_Profiles
    template_name = "Profiles/schoolSettings.html"

    def get_context_data(self, **kwargs):
        slug = self.kwargs.get("slug")
        context = super().get_context_data(**kwargs)
        current_school = context["school"]
        context["all_classes"] = SchoolClass.objects.all()
        context["all_formats"] = SchoolFormat.objects.all()
        context["all_types"] = SchoolType.objects.all()
        context["all_boards"] = SchoolBoard.objects.all()
        context["all_country"] = Country.objects.all()
        context["all_state"] = State.objects.all()
        context["all_city"] = City.objects.all()
        context["admission_classes"] = AdmissionOpenClasses.objects.filter(
            school=current_school
        )
        context["school_slug"] = slug
        return context


class SchoolDetailsUpdateView(LoginRequiredMixin, SchoolTest, UpdateView):
    model = School_Profiles
    form_class = forms.SchoolDetailsUpdateForm
    template_name = "Profiles/schoolSettings.html"

    def get_success_url(self):
        return reverse("Profiles:schoolSettings", kwargs={"slug": self.object.slug})

    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        print(form.errors)
        return super().form_invalid(form)

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        user = User.objects.get(email=email)
        user.first_name = form.cleaned_data.get("school_name")
        user.save()
        print("success")
        return super().form_valid(form)


class UploadLogoView(LoginRequiredMixin, SchoolTest, UpdateView):
    model = School_Profiles
    form_class = forms.LogoForm
    template_name = "Profiles/schoolSettings.html"

    def get_success_url(self) -> str:
        return reverse("Profiles:schoolSettings", kwargs={"slug": self.object.slug})

    def form_valid(self, form):
        school_profile = self.get_object()
        old_logo_path = school_profile.logo.path
        if os.path.exists(old_logo_path):
            os.remove(old_logo_path)
        form.save()
        return super().form_valid(form)


class AvailableClassSetView(LoginRequiredMixin, SchoolTest, UpdateView):
    model = School_Profiles
    form_class = forms.AvailableClassForm
    template_name = "Profiles/schoolSettings.html"

    def get_success_url(self) -> str:
        return reverse("Profiles:schoolSettings", kwargs={"slug": self.object.slug})


class SchoolFacilitiesUpdateView(UpdateView):
    model = SchoolFacilities
    form_class = forms.SchoolFacilitiesForm
    template_name = "Profiles/schoolSettings.html"

    def get_success_url(self) -> str:
        school = self.object.school_profiles
        return reverse("Profiles:schoolSettings", kwargs={"slug": school.slug})

    def get_context_data(self, **kwargs):
        # Override this method to add extra context data
        attribute_names = [field.name for field in SchoolFacilities._meta.get_fields()]
        print(attribute_names)
        context = super().get_context_data(**kwargs)
        context["attribute_names"] = attribute_names
        return context


#     def get_success_url(self) -> str:
#         school = self.object.school_profiles
#         return reverse("Profiles:schoolSettings", kwargs={"slug": school.slug})

#     def form_invalid(self, form: BaseModelForm) -> HttpResponse:
#         print(form.errors)
#         return super().form_invalid(form)

#     def form_valid(self, form: BaseModelForm) -> HttpResponse:
#         print("sssssssssssssssssssssssssssss")
#         return super().form_valid(form)


# Function Views


def userTypeTest(user):
    return user.is_school


def index(request):
    featured_school_list = School_Profiles.objects.filter(is_featured=True)
    school_format = SchoolFormat.objects.all()
    context_dict = {
        "school_data": featured_school_list,
        "school_format": school_format,
    }
    return render(request, "Profiles/index.html", context_dict)


def register(request):
    if request.method == "POST":
        form_response = forms.AddSchoolForm(request.POST)
        user_response = forms.UserForm(request.POST)

        if form_response.is_valid() and user_response.is_valid():
            school_profile = School_Profiles()
            school_profile.school_name = form_response.cleaned_data["school_name"]
            school_profile.email = form_response.cleaned_data["email"]
            school_profile.number = form_response.cleaned_data["number"]
            school_profile.address = form_response.cleaned_data["address"]
            school_profile.city = form_response.cleaned_data["city"]
            school_profile.state = form_response.cleaned_data["state"]
            school_profile.country = form_response.cleaned_data["country"]

            user = User()
            user.username = form_response.cleaned_data["email"]
            user.email = form_response.cleaned_data["email"]
            user.first_name = form_response.cleaned_data["school_name"]
            user.is_school = True
            user.set_password(user_response.cleaned_data["password"])
            user.save()
            school_profile.user = user
            school_profile.save()

            return redirect("Profiles:index")
        else:
            print("Invalid Form Response")
            print(form_response.errors)
            print(user_response.errors)
    else:
        form_response = forms.AddSchoolForm()
        user_response = forms.UserForm()

    city_list = City.objects.all().order_by("city_name")
    state_list = State.objects.all().order_by("state_name")
    country_list = Country.objects.all().order_by("country_name")

    formDict = {
        "RegistrationForm": form_response,
        "RegisterUser": user_response,
        "city_list": city_list,
        "state_list": state_list,
        "country_list": country_list,
    }
    return render(request, "Profiles/register.html", context=formDict)


def user_login(request):
    if request.method == "POST":
        email = request.POST.get("useremail")
        password = request.POST.get("password")
        user = authenticate(username=email, password=password)

        if user:
            if user.is_active:
                login(request, user)
                print(user)
                return redirect("Profiles:index")
            else:
                messages.error(request, "Account is not active", extra_tags="login")
        else:
            messages.error(
                request, "Incorrect Username or Password", extra_tags="login"
            )
    return redirect("Profiles:index")


@login_required
def user_logout(request):
    logout(request)
    return redirect("Profiles:index")


@user_passes_test(userTypeTest)
def SchoolAdmissionOpenView(request, slug):
    user = request.user
    if request.method == "POST":
        school_id = request.POST.get("school")
        school = School_Profiles.objects.get(id=school_id)
        class_id = request.POST.get("class_opened")
        opened_class = SchoolClass.objects.get(id=class_id)
        admission_class_obj, created = AdmissionOpenClasses.objects.get_or_create(
            school=school, class_opened=opened_class
        )
        admission_class_obj.form_limit = request.POST.get("form_limit")
        admission_class_obj.form_price = request.POST.get("form_price")
        admission_class_obj.status = request.POST.get("status")
        admission_class_obj.save()
    return HttpResponseRedirect(
        reverse("Profiles:schoolSettings", kwargs={"slug": slug})
    )
