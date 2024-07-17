from django.urls import path
from Profiles.api.views import (
    CountryListView, StateListView, CityListView, 
    SchoolTypeListView, SchoolFormatListView, SchoolBoardListView,
    SchoolClassListView, SchoolProfilesListView, SchoolFacilitiesListView,
    SchoolProfileDetailView
)

app_name = "schools"

urlpatterns=[
    path("",SchoolProfilesListView.as_view(),name="school-list"),
    path("profile/<slug:slug>/", SchoolProfileDetailView.as_view(), name="school-detail"),
    path("classes/",SchoolClassListView.as_view(),name="all-classes"),
    path("countries/", CountryListView.as_view(), name="country-list"),
    path("states/", StateListView.as_view(), name="state-list"),
    path("cities/", CityListView.as_view(), name="city-list"),
    path("school-types/", SchoolTypeListView.as_view(), name="school-type-list"),
    path("school-formats/", SchoolFormatListView.as_view(), name="school-format-list"),
    path("school-boards/", SchoolBoardListView.as_view(), name="school-board-list"),
    path("school-facilities/", SchoolFacilitiesListView.as_view(), name="school-facility-list"),
]