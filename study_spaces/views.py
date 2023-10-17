from django.shortcuts import render, redirect
from django.contrib.auth import logout


def home(request):
    if request.user.is_authenticated:
        admins = ['lukecreech11@gmail.com', 'rqf8pe@virginia.edu']
        email = request.user.email
        if email in admins:
            return redirect('/study/admin')
        else:
            return render(request, "study_spaces/user.html")
    else:
        return redirect("/study/login")


def logout_view(request):
    logout(request)
    return redirect("/study")

def login_view(request):
    if request.user.is_authenticated:
        return redirect("/study")
    else:
    	return render(request, "study_spaces/login.html")
    
def admin_view(request):
	if request.user.is_authenticated:
		return render(request, "study_spaces/admin.html")
	else:
		return redirect('/study/login')
    
