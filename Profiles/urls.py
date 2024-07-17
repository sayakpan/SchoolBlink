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
    path("school/settings/<slug:slug>",views.SchoolSettingsView.as_view(),name="schoolSettings",),
    path("school/update/<slug:slug>",views.SchoolDetailsUpdateView.as_view(),name="schoolUpdate",),
    path("school/uploadlogo/<slug:slug>",views.UploadLogoView.as_view(),name="uploadlogo",),
    path("school/updateclass/<slug:slug>",views.AvailableClassSetView.as_view(),name="updateclass",),
    path("school/changeadmission/<slug:slug>",views.SchoolAdmissionOpenView,name="changeadmission",),
    path("school/changefacilities/<slug:slug>",views.SchoolFacilitiesUpdateView.as_view(),name="changefacilities",),
]
