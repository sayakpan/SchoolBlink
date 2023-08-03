from django.urls import path
from Profiles.api.views import SchoolProfilesListView

app_name = "school"

urlpatterns=[
    path("",SchoolProfilesListView.as_view(),name="school-list"),
]