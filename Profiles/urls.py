"""SchoolData URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Profiles import views

app_name = "Profiles"

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("explore/", views.Explore.as_view(), name="explore"),
    path("explore/<slug:slug>", views.CustomExplore.as_view(), name="customExplore"),
    path("login/", views.user_login, name="loginPage"),
    path("logout/", views.user_logout, name="logoutPage"),
    path("signup/", views.ParentSignUpView.as_view(), name="signup"),
    path("school/<slug:slug>", views.ProfileView.as_view(), name="schoolProfile"),
    path(
        "school/settings/<slug:slug>",
        views.SchoolSettingsView.as_view(),
        name="schoolSettings",
    ),
    path(
        "school/update/<slug:slug>",
        views.SchoolDetailsUpdateView.as_view(),
        name="schoolUpdate",
    ),
    path(
        "school/uploadlogo/<slug:slug>",
        views.UploadLogoView.as_view(),
        name="uploadlogo",
    ),
    path(
        "school/updateclass/<slug:slug>",
        views.AvailableClassSetView.as_view(),
        name="updateclass",
    ),
    path(
        "school/changeadmission/<slug:slug>",
        views.SchoolAdmissionOpenView,
        name="changeadmission",
    ),
    path(
        "school/changefacilities/<slug:slug>",
        views.SchoolFacilitiesUpdateView.as_view(),
        name="changefacilities",
    ),
]
