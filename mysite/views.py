from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User

def user_login(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('/blog/')
		else:
			return redirect('/login/')
	else:
	 	return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('/blog/')

def ajax_login(request):
    username = request.GET['username']
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        user_exists = '0'   
        return HttpResponse(str(user_exists))
    user_exists = '1'
    return HttpResponse(str(user_exists))

def show_index_page(request):
    return render(request, 'index.html')
