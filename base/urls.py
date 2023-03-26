from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("profile/<str:name>", views.profile, name="profile"),
    path("newyear", views.newyear, name="newyear"),
]