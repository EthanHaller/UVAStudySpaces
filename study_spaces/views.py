from django.shortcuts import render


def home(request):
    return render(request, "study_spaces/homepage.html")
