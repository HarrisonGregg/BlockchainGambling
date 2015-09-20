from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from django.template import RequestContext
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def bet(request):
	error = ''
	form = BetForm()
	bets = Bet.objects.filter(user=request.user)

	return render(request, 'frontend/bet.html', context_instance=RequestContext(request, {'form':form, 'error':error, 'bets':bets}))

@login_required(login_url='/')
def logout_view(request):
	logout(request)
	return HttpResponseRedirect("/")

@login_required(login_url='/')
def start(request):
	error = ""
	if request.method == 'POST':
		name = request.POST.get("name", None)
		fee = request.POST.get("fee", None)
		if name and fee:
			league = League(name=name,fee=fee,admin=request.user)
			league.save()
			return HttpResponseRedirect("/join/"+name+"/")

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

@login_required(login_url='/')
def join(request):
	return joinLeague(request,"")

@login_required(login_url='/')
def joinLeague(request, league_name):
	error = ""
	if request.method == 'POST':
		league_name = request.POST.get("league_name", None)
		campaign = request.POST.get("campaign", None)
		if league_name and campaign:
			try:
				league = League.objects.get(name=league_name)
				bet = Bet(league=league, user=request.user, campaign=campaign) 
				bet.save()
				return HttpResponseRedirect("/bet/")
			except DoesNotExist:
				error = "League not found."
		else:
			error = "Please enter a valid team and GoFundMe URL"

	form = JoinForm(auto_id=False)
	return render(request, 'frontend/join.html', context_instance=RequestContext(request, {'form': form, 'error': error}))

def signup(request):
	error = ""
	if request.method == 'POST':
		username = request.POST.get("username", None)
		email = request.POST.get("email", None)
		password = request.POST.get("password", None)
		if username and email and password and league_name:
			user = User(username=username, email=email, password=password)
			try:
				user.save()
				return HttpResponseRedirect("/")
			except IntegrityError:
				error = "Please choose another name."
		else: 
			error = "Please fill out all fields."

	form = SignupForm(auto_id=False)
	return render(request, 'frontend/signup.html', context_instance=RequestContext(request, {'form': form, 'error' : error}))
