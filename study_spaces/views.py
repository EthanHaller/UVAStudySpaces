from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.conf import settings
from .mixins import Directions

def home(request):
    if request.user.is_authenticated:
        admins = ['lukecreech11@gmail.com', 'rqf8pe@virginia.edu']
        email = request.user.email
        if email in admins:
            return render(request, "study_spaces/admin.html")
    return render(request, "study_spaces/homepage.html")


def logout_view(request):
    logout(request)
    return redirect("/study/")

def map(request):

    # Code taken from https://www.youtube.com/watch?v=wCn8WND-JpU

	lat_a = request.GET.get("lat_a")
	long_a = request.GET.get("long_a")
	lat_b = request.GET.get("lat_b")
	long_b = request.GET.get("long_b")
	directions = Directions(
		lat_a= lat_a,
		long_a=long_a,
		lat_b = lat_b,
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

def route(request):
	context = {"google_api_key": settings.GOOGLE_API_KEY}
	return render(request, 'study_spaces/route.html', context)