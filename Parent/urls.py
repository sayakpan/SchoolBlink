from django.contrib import admin
from django.urls import path
from Parent import views

app_name = "Parent"

urlpatterns = [
    path("user/<slug:slug>", views.ParentProfileView.as_view(), name="parentProfile"),
    path(
        "change/account/<slug:slug>",
        views.AccountUpdateView.as_view(),
        name="accountupdate",
    ),
    path(
        "change/personal/<slug:slug>",
        views.PersonalDataUpdateView.as_view(),
        name="personalupdate",
    ),
    path(
        "upload/<slug:slug>",
        views.UploadProfilePictureView.as_view(),
        name="uploadprofilepicture",
    ),
    path(
        "reset/<slug:slug>",
        views.ResetPasswordView,
        name="resetpassword",
    ),
    path(
        "addchild/<slug:slug>",
        views.AddChildProfileView,
        name="addchild",
    ),
    path(
        "updatechild/<slug:slug>",
        views.UpdateChildProfileView,
        name="updatechild",
    ),
    path(
        "deletechild/<int:pk>",
        views.DeleteChildProfileView.as_view(),
        name="deletechild",
    ),
]
