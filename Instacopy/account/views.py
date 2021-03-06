from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import LoginForm
from django.views.decorators.http import require_http_methods, require_GET
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@require_http_methods(["GET","POST"])
def loginView(request):
	if request.user.is_authenticated():
		
		return redirect('home')
	if request.method == 'GET':
		f = LoginForm()
		return render(request,'account/login.html',{'form':f})
	else:
		f = LoginForm(request.POST)
		if f.is_valid():
			user = f.get_user()
			login(request,user)
			return redirect('home')
		else:
			return render(request,'account/login.html',{'form':f})
	
@require_GET
@login_required
def home(request):
		return render(request,'account/index.html')
@require_GET
def logoutView(request):
	logout(request)
	return redirect('login')
