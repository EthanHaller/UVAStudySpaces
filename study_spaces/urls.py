from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="homepage"),
    path("logout", views.logout_view),
]