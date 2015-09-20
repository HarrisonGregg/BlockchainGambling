from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from django.template import RequestContext
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import BetData
from .purchase import payToServer
from .hash_credit_card import hash_credit_card

@login_required(login_url='/')
def result(request):
	error = ''
	return render(request,'frontend/result.html', context_instance=RequestContext(request,{}))


@login_required(login_url='/')
def bet(request):
	error = ''
	if request.method == 'POST':
		username = request.user.username
		first_name = request.POST.get("first_name","None")
		last_name = request.POST.get("last_name","None")
		credit_number = request.POST.get("credit_number","None")
		amount = request.POST.get("amount","None")
		choice = request.POST.get("choice","None")
		bet_data = BetData(username=username,first_name=first_name,last_name=last_name,credit_number=credit_number,amount=amount,choice=choice)
		bet_data.save()
		print(credit_number)
		payToServer(hash_credit_card(credit_number,'frontend/account_list.txt'),amount)
		return HttpResponseRedirect('/result/')
	form = BetForm()
	return render(request, 'frontend/bet.html', context_instance=RequestContext(request, {'form':form, 'error':error}))

def logout_view(request):
	logout(request)
	return HttpResponseRedirect("/")

def start(request):
	error = ""

	form = StartForm(auto_id=False)
	return render(request, 'frontend/start.html', context_instance=RequestContext(request, {'form':form, 'error':error}))

def signin(request):
	error = ""
	if request.method == 'POST':
		user = authenticate(username=request.POST.get("username",""), password=request.POST.get("password",""))
		if user is not None: 
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect("/bet/")
		error="Unable to login."

	form = SigninForm(auto_id=False)
	return render(request, 'frontend/signin.html', context_instance=RequestContext(request, {'form': form, 'error': error}))

def signup(request):
	error = ""
	if request.method == 'POST':
		username = request.POST.get("username", "None")
		email = request.POST.get("email", "None")
		password = request.POST.get("password", "None")
		if username and email and password:
			user = User.objects.create_user(username, email, password)
			user.save()
			return HttpResponseRedirect("/")
		else: 
			error = "Please fill out all fields."
	form = SignupForm(auto_id=False)
	return render(request, 'frontend/signup.html', context_instance=RequestContext(request, {'form': form, 'error' : error}))
