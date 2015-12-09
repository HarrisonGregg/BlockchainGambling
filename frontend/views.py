from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from django.template import RequestContext
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import BetData, GameBet
from scraper.models import Team, Game
import random, datetime
from django.core.mail import send_mail
from django.db import IntegrityError

@login_required(login_url='/')
def bet(request):
	error = ''

	open_bets = GameBet.objects.filter(acceptor__isnull=True,completed=False).exclude(creator=request.user)
	my_game_bets = GameBet.objects.filter(creator=request.user)
	accepted_bets = GameBet.objects.filter(acceptor=request.user)

	if request.method == 'POST':
		selected_team = get_object_or_404(Team, pk = request.POST.get('team_id'))
		user.team = selected_team
		user.save()

	return render(request, 'frontend/bet.html', context_instance=RequestContext(request, {'error':error, 'open_bets':open_bets, 'my_game_bets':my_game_bets, 'accepted_bets':accepted_bets}))

@login_required(login_url='/')
def accept_bet(request,bet_id):
	game_bet = GameBet.objects.get(id=bet_id)
	game_bet.acceptor = request.user 
	game_bet.save()
	return HttpResponseRedirect('/bet/')

@login_required(login_url='/')
def logout_view(request):
	logout(request)
	return HttpResponseRedirect("/")

@login_required(login_url='/')
def start(request):
	error = ""

	upcoming_games = Game.objects.filter(date__gt=datetime.date.today()).order_by('date')[:10]

	if request.method == 'POST':
		val = request.POST.get("game", None).split(" ",1)

		game_id = val[0]
		amount = request.POST.get("amount", None)
		if game_id and amount:
			try:
				game = Game.objects.get(id=game_id)
				winning_team = val[1]

				game_bet = GameBet(creator=request.user, game=game, amount=amount, winner=winning_team)
				game_bet.save()
				return HttpResponseRedirect("/bet/")
			except Exception as e:
				# error = "League name taken."
				error = e

	form = StartForm(auto_id=False)
	# print render(request, 'frontend/start.html', context_instance=RequestContext(request, {'form':form, 'error':error, 'upcoming_games':upcoming_games}))
	return render(request, 'frontend/start.html', context_instance=RequestContext(request, {'form':form, 'error':error, 'upcoming_games':upcoming_games}))

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
				send_mail('Welcome!', 'Hi '+user.username +', welcome to BlockLeague! ', 'blockleagueofficial@gmail.com', [user.email])
				return HttpResponseRedirect("/")
			except IntegrityError:
				error = "Please choose another name."
		else: 
			error = "Please fill out all fields."

	form = SignupForm(auto_id=False)
	return render(request, 'frontend/signup.html', context_instance=RequestContext(request, {'form': form, 'error' : error}))

def updateBets():
	for bet in GameBet.objects.filter(completed=False,game__date__lte=datetime.date.today()):
		if bet.game.gameId:
			bet.completed = True
			if bet.game.home_team_score == bet.game.visit_team_score or not bet.acceptor:
				pass
			elif (bet.winner == bet.game.home_team) == (bet.game.home_team_score > bet.game.visit_team_score):
				bet.won = True
			else:
				bet.won = False
			bet.save()
	return HttpResponse("success!")
