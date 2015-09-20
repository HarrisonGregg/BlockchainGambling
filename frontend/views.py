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
from .models import BetData
from .purchase import payToServer
from .hash_credit_card import hash_credit_card
import random, datetime
from .donate import userWin,userLost

def send_money(user0,user1):
	for user in user0:
		userWin(user.credit_number,user.amount)
	for user in user1:
		userLost('55fda9d43c3ce2100041183e',user.amount)

@login_required(login_url='/')
def congrats(request):
	return render(request,'frontend/congrats.html', context_instance=RequestContext(request,{}))

@login_required(login_url='/')
def result(request):
	user0 = BetData.objects.filter(choice=u'Heads')
	user1 = BetData.objects.filter(choice=u'Tails')
	random.seed(datetime.time.second)
	result = 1#random.randint(0, 1)
	if result == 0:
		send_money(user0,user1)
		result_str = 'You Win!'
	else:
		send_money(user1,user0)	
		result_str = 'You Lost'
	return render(request,'frontend/result.html', context_instance=RequestContext(request,{'result':result_str}))


@login_required(login_url='/')
def bet(request):
	error = ''
	if request.method == 'POST':
		username = request.user.username
		first_name = request.POST.get("first_name","None")
		last_name = request.POST.get("last_name","None")
		credit_number = hash_credit_card(request.POST.get("credit_number","None"),'frontend/account_list.txt')
		amount = request.POST.get("amount","None")
		choice = request.POST.get("choice","None")
		bet_data = BetData(username=username,first_name=first_name,last_name=last_name,credit_number=credit_number,amount=amount,choice=choice)
		bet_data.save()
		#print(credit_number)
		payToServer(credit_number,amount)
		return HttpResponseRedirect('/congrats/')
	form = BetForm()
	bets = Bet.objects.filter(user=request.user)

	return render(request, 'frontend/bet.html', context_instance=RequestContext(request, {'form':form, 'error':error, 'bets':bets}))
	return render(request, 'frontend/bet.html', context_instance=RequestContext(request, {'form':form, 'error':error}))

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
