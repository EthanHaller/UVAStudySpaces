from django.shortcuts import render, redirect
from django.contrib.auth import logout


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
