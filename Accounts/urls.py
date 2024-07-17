from django.urls import path
from .views import ParentSignupView, SchoolLoginView, ParentLoginView, SchoolSignupView

urlpatterns = [
    path('signup/school/', SchoolSignupView.as_view(), name='school-signup'),
    path('signup/parent/', ParentSignupView.as_view(), name='parent-signup'),
    path('login/school/', SchoolLoginView.as_view(), name='school-login'),
    path('login/parent/', ParentLoginView.as_view(), name='parent-login'),
]
