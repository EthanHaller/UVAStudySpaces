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


def get_approved_spaces():
    return StudySpace.objects.filter(approved_submission=StudySpace.ApprovalStatus.APPROVED)


def get_pending_spaces():
    return StudySpace.objects.filter(approved_submission=StudySpace.ApprovalStatus.PENDING)


def get_spaces_by_email(email):
    return StudySpace.objects.filter(user_email=email)


@login_required(login_url='/study/login')
def home(request):
    mod = get_approved_spaces()
    mod_json = json.dumps(list(mod.values('latitude', 'longitude', 'id', 'name')))
    return render(request, "study_spaces/studyspaces.html", {'mod': mod, 'mod_json': mod_json, 'key': 'AIzaSyC5DCptRFmVd168TUsP-5pe0etKaeGNCEY'})


def logout_view(request):
    logout(request)
    return redirect("/study/")

@login_required(login_url='/study/login')
def directions(request):
    # Code taken from https://www.youtube.com/watch?v=wCn8WND-JpU
    mod_json = []
    s = None
    if "dest" in request.GET:
        s = StudySpace.objects.get(pk=request.GET["dest"])
        s = {'latitude': s.latitude, 'longitude': s.longitude, 'id': s.id, 'name': s.name, 'address': s.address}
        mod_json = json.dumps(s)

    lat_a = request.GET.get("lat_a")
    long_a = request.GET.get("long_a")
    lat_b = request.GET.get("lat_b")
    long_b = request.GET.get("long_b")
    directions = None
    showDirections = False
    if lat_a and long_a and lat_b and long_b:
        directions = Directions(
            lat_a=lat_a,
            long_a=long_a,
            lat_b=lat_b,
            long_b=long_b,
        )
        showDirections = True
    return render(request, 'study_spaces/directions.html', {'s': s, 'mod_json': mod_json, 'key': 'AIzaSyC5DCptRFmVd168TUsP-5pe0etKaeGNCEY', 'directions': directions, 'showDirections': showDirections, "origin": f'{lat_a}, {long_a}', "destination": f'{lat_b}, {long_b}'})


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


# https://stackoverflow.com/questions/2140550/how-to-require-login-for-django-generic-views
class IndexView(LoginRequiredMixin, generic.ListView):
    login_url = '/study/login'
    redirect_field_name = 'next'
    template_name = "study_spaces/index.html"
    context_object_name = "study_space_list"

    def get_queryset(self):
        return get_approved_spaces()


@login_required(login_url='/study/login')
def profile(request):
    if is_admin(request.user.email):
        return render(request, 'study_spaces/admin.html')
    return render(request, 'study_spaces/profile.html')


@login_required(login_url='/study/login')
def submission(request):
    context = {"google_api_key": settings.GOOGLE_API_KEY}
    if is_admin(request.user.email):
        context["pending_list"] = get_pending_spaces()
        return render(request, 'study_spaces/approval.html', context)
    else:
        context["submitted_list"] = get_spaces_by_email(request.user.email)
        if request.method == 'POST':
            if request.POST["name"] == '':
                context["error_message"] = "Please input a name."
                return render(request, 'study_spaces/submission.html', context)
            if request.POST["address"] == '' or request.POST["lat"] == '' or request.POST["long"] == '':
                context["error_message"] = "Please input a valid address."
                return render(request, 'study_spaces/submission.html', context)
            s = StudySpace(
                name=request.POST["name"],
                address=request.POST["address"],
                latitude=request.POST["lat"],
                longitude=request.POST["long"],
                user_email=request.user.email
            )
            s.save()
        context["submitted_list"] = get_spaces_by_email(request.user.email)
        return render(request, 'study_spaces/submission.html', context)


@login_required(login_url='/study/login')
def approve_submission(request):
    if request.method == 'POST':
        s = StudySpace.objects.get(pk=request.POST["id"])
        s.approved_submission = StudySpace.ApprovalStatus.APPROVED
        s.save()
    return redirect('/study/submission')


def deny_submission(request):
    if request.method == 'POST':
        s = StudySpace.objects.get(pk=request.POST["id"])
        s.approved_submission = StudySpace.ApprovalStatus.DENIED
        s.denial_reason = request.POST["Denial"]
        s.save()
    return redirect('/study/submission')

@login_required(login_url='/study/login')
def information(request):
    context = {}
    if "dest" in request.GET:
        s = StudySpace.objects.get(pk=request.GET["dest"])
        dest = s.information
        context["dest_information"] = dest
    return render(request, 'study_spaces/information.html', context)
