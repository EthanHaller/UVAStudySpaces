from django.urls import path

from . import views


app_name = "study_spaces"
urlpatterns = [
    path("", views.home, name="homepage"),
    path("logout", views.logout_view, name="logout"),
    path('login', views.login_view),
    path('admin', views.admin_view)
]