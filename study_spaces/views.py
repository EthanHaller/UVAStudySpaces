from django.shortcuts import render, redirect
from django.contrib.auth import logout
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
    return redirect("/study")

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
    
