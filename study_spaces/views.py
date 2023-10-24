from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.conf import settings
from django.utils.decorators import method_decorator

from .mixins import Directions
from django.contrib.auth.decorators import login_required
from django.views import generic
import json

from .models import *


def is_admin(email):
    admins = [
        'lukecreech11@gmail.com',
        'rqf8pe@virginia.edu'
    ]

    return email in admins


@login_required(login_url='/study/login')
def home(request):
    mod = StudySpace.objects.all()
    mod_json = json.dumps(list(mod.values('latitude', 'longitude')))
    return render(request, "study_spaces/studyspaces.html", {'mod': mod, 'mod_json': mod_json, 'key': 'AIzaSyC5DCptRFmVd168TUsP-5pe0etKaeGNCEY'})


def logout_view(request):
    logout(request)
    return redirect("/study/")


@login_required(login_url='/study/login')
def map(request):
    # Code taken from https://www.youtube.com/watch?v=wCn8WND-JpU
    if ("lat_a" not in request.GET
            or "long_a" not in request.GET
            or "lat_b" not in request.GET
            or "long_b" not in request.GET):
        return redirect("/study/route")
    lat_a = request.GET.get("lat_a")
    long_a = request.GET.get("long_a")
    lat_b = request.GET.get("lat_b")
    long_b = request.GET.get("long_b")
    directions = Directions(
        lat_a=lat_a,
        long_a=long_a,
        lat_b=lat_b,
        long_b=long_b
    )

    context = {
        "google_api_key": settings.GOOGLE_API_KEY,
        "lat_a": lat_a,
        "long_a": long_a,
        "lat_b": lat_b,
        "long_b": long_b,
        "origin": f'{lat_a}, {long_a}',
        "destination": f'{lat_b}, {long_b}',
        "directions": directions,

    }
    return render(request, 'study_spaces/map.html', context)


@login_required(login_url='/study/login')
def route(request):
    # Code taken from https://www.youtube.com/watch?v=wCn8WND-JpU
    context = {"google_api_key": settings.GOOGLE_API_KEY}
    if "dest" in request.GET:
        s = StudySpace.objects.get(pk=request.GET["dest"])
        dest = s.address
        context["dest_address"] =  dest
    return render(request, 'study_spaces/route.html', context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect("/study")
    else:
        return render(request, "study_spaces/login.html")


@login_required(login_url='/study/login')
def admin_view(request):
    if is_admin(request.user.email):
        return render(request, "study_spaces/admin.html")
    else:
        return redirect('/study')


#https://stackoverflow.com/questions/2140550/how-to-require-login-for-django-generic-views
class IndexView(LoginRequiredMixin, generic.ListView):
    login_url = '/study/login'
    redirect_field_name = 'next'
    template_name = "study_spaces/index.html"
    context_object_name = "study_space_list"

    def get_queryset(self):
        return StudySpace.objects.all()

@login_required(login_url='/study/login')
def profile(request):
    if is_admin(request.user.email):
        return render(request, 'study_spaces/admin.html')
    return render(request, 'study_spaces/profile.html')



