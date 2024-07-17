from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from Profiles import views

urlpatterns = [
    path("", views.index, name="index"),
    path("admin/", admin.site.urls),
    path("profiles/", include("Profiles.urls")),
    path("parent/", include("Parent.urls")),
    path("admissions/", include("Admissions.urls")),
    path('accounts/', include('Accounts.urls')),

    # Rest API URLS
    path("api/school/", include("Profiles.api.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
