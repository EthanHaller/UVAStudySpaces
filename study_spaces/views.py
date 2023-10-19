from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.conf import settings
from .mixins import Directions
from django.contrib.auth.decorators import login_required


def is_admin(email):
    admins = [
        'lukecreech11@gmail.com',
        'rqf8pe@virginia.edu'
    ]

    return email in admins


@login_required(login_url='/study/login')
def home(request):
    if is_admin(request.user.email):
        return redirect('/study/admin')
    else:
        return render(request, "study_spaces/user.html")


def logout_view(request):
    logout(request)
    return redirect("/study/")


@login_required(login_url='/study/login')
def map(request):
    # Code taken from https://www.youtube.com/watch?v=wCn8WND-JpU
    if "lat_a" not in request or "long_a" not in request or "lat_b" not in request or "long_b" not in request:
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
