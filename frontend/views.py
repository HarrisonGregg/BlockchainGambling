from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from django.template import RequestContext
from .forms import *
from .models import *
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import BetData
from scraper.models import Team
from .purchase import payToServer
from .hash_credit_card import hash_credit_card
import random, datetime
from .donate import userWin,userLost

# def send_money(user0,user1):
# 	for user in user0:
# 		card = CreditCard.objects.get(user=user)
# 		userWin(card.number,user.amount)
# 	for user in user1:
# 		userLost('55fda9d43c3ce2100041183e',user.amount)

def send_to_charity(user, amount):
	userLost('55fda9d43c3ce2100041183e',amount)

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

def betResult(request, bet_id):
	bet = Bet.objects.get(id=bet_id)
	return render(request,'frontend/result.html', context_instance=RequestContext(request,{'result':bet.result}))


@login_required(login_url='/')
def bet(request):
	error = ''

	teams = Team.objects.all()

	if request.method == 'POST':
		selected_team = get_object_or_404(Team, pk = request.POST.get('team_id'))
		user.team = selected_team
		user.save()
	return render(request, 'frontend/NBApage.html', context_instance=RequestContext(request, {'error':error, 'teams':teams}))

@login_required(login_url='/')
def add_card(request):
	error = ''
	if request.method == 'POST':
		user = request.user
		user.first_name = request.POST.get("first_name","None")
		user.last_name = request.POST.get("last_name","None")
		card = None
		try:
			card = CreditCard.objects.get(user=user)
		except:
			card = CreditCard(number=hash_credit_card(request.POST.get("credit_number","None"),'frontend/account_list.txt'), user=user)
			card.save()
		user.save()
		return HttpResponseRedirect('/bet/')
	form = AddCardForm()

	return render(request, 'frontend/add_card.html', context_instance=RequestContext(request, {'form':form, 'error':error}))

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
			try:
				league = League(name=name,fee=fee,admin=request.user)
				league.save()
				return HttpResponseRedirect("/join/"+name+"/")
			except:
				error = "League name taken."

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
		# campaign = request.POST.get("campaign", None)
		if league_name:# and campaign:
			try:
				try:
					card = CreditCard.objects.get(user=request.user)
					league = League.objects.get(name=league_name)
					bet = Bet(league=league, user=request.user, campaign="") 
					bet.save()
					payToServer(card.number,league.fee)

					return HttpResponseRedirect("/bet/")
				except (CreditCard.DoesNotExist):
					error = "Please add a credit card"
			except League.DoesNotExist:
				error = "League not found."
		else:
			error = "Please enter a valid team and GoFundMe URL"

	form = JoinForm(auto_id=False, initial={'league_name': league_name})
	return render(request, 'frontend/join.html', context_instance=RequestContext(request, {'form': form, 'error': error, 'league_name':league_name}))

@login_required(login_url='/')
def manage(request, league_id):
	error = ""
	league = League.objects.get(id=league_id)
	bets = Bet.objects.filter(league=league)
	if request.method == 'POST':
		random.seed(datetime.time.second)
		winner = random.randint(0,len(bets)-1)
		for i, bet in enumerate(bets):
			if i == winner:
				bet.result = "You won $" + str(len(bets)*league.fee) + "!"
			else:
				bet.result = "You lost :("#, but your money went to " + bets[winner].campaign + "!"
				user = bet.user
				send_to_charity(user,league.fee)
			bet.save()
		return HttpResponseRedirect("/bet/")


	return render(request, 'frontend/manage.html', context_instance=RequestContext(request, {'error': error, 'bets':bets}))

def signup(request):
	error = ""
	if request.method == 'POST':
		username = request.POST.get("username", None)
		email = request.POST.get("email", None)
		password = request.POST.get("password", None)
		if username and email and password:
			user = User.objects.create_user(username=username, email=email, password=password)
			try:
				user.save()
				return HttpResponseRedirect("/")
			except IntegrityError:
				error = "Please choose another name."
		else: 
			error = "Please fill out all fields."

	form = SignupForm(auto_id=False)
	return render(request, 'frontend/signup.html', context_instance=RequestContext(request, {'form': form, 'error' : error}))
