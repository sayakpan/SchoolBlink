from django.contrib import admin
from django.urls import path
from Admissions import views

app_name = "Admissions"

urlpatterns = [
    path(
        "application/<slug:slug>/<int:class_id>",
        views.SchoolApplicationView.as_view(),
        name="application",
    ),
    path(
        "application/<slug:slug>/<int:class_id>/submit",
        views.SchoolApplicationSubmitView.as_view(),
        name="applicationsubmit",
    ),
    path(
        "application/<int:pk>/checkout",
        views.SchoolApplicationPaymentView.as_view(),
        name="checkout",
    ),
    path(
        "application/<int:pk>/paymenthandler/",
        views.paymenthandler,
        name="paymenthandler",
    ),
]
