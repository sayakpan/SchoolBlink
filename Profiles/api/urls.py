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
    path("types/", SchoolTypeListView.as_view(), name="type-list"),
    path("formats/", SchoolFormatListView.as_view(), name="format-list"),
    path("boards/", SchoolBoardListView.as_view(), name="board-list"),
    path("facilities/", SchoolFacilitiesListView.as_view(), name="facility-list"),
]