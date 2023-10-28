from django.urls import path

from . import views


app_name = "study_spaces"
urlpatterns = [
    path("", views.home, name="homepage"),
    path("logout", views.logout_view, name="logout"),
    path('login', views.login_view, name="login"),
    path('admin', views.admin_view, name="admin"),
    path('route', views.route, name="route"),
    path('map', views.map, name="map"),
    path('index', views.IndexView.as_view(), name="index"),
    path('profile', views.profile, name='profile'),
    path('submission', views.submission, name='submission')
]
