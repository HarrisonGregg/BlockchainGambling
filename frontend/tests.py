from .views import signin, signup, bet, accept_bet, updateBets, make_bet
from .models import GameBet
from scraper.models import Game
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser, User
from django.contrib.auth import authenticate, login, logout
from datetime import date
from scraper.views import updateNBAteams, updateNBAgames

class TestSigninMethods(TestCase):

	def setUp(self):
		# Every test needs access to the request factory. 
		self.factory = RequestFactory()
		self.user = User.objects.create_user(username = 'haiwei', email = 'haiwei@...', password = 'top_secret')

		updateNBAteams()
		updateNBAgames(test=True)

		game = Game.objects.all()[0]
		bet = GameBet(creator=self.user, game=game, amount=10, winner=game.home_team)
		bet.save()

	def test_signup(self):
		request = self.factory.post('/signup/',{"username":"anon","password":"password","email":"anon@example.com"})

		response = signup(request)

		self.assertEqual(response.status_code, 302)

		user = authenticate(username="anon", password="password")

		self.assertIsNotNone(user)

	def test_sign_in(self):
		request = RequestFactory().post(
			"/signin/", {"username": "", "password": ""})
		request.session = {}

		response = signin(request)

		self.assertEqual(response.status_code, 200)

	def test_bet(self):
		request = self.factory.get('/bet/')
		request.user = self.user
		response = bet(request)

		self.assertEqual(response.status_code, 200)

	def test_scraper(self):
		updateNBAteams()
		updateNBAgames(test=True)

	def test_accept_bet(self):
		bet = GameBet.objects.all()[0]

		request = self.factory.post('/bet/',{})
		request.user = self.user

		response = accept_bet(request, bet.id)

		self.assertEqual(response.status_code, 302)

	def test_make_bet(self):
		request = self.factory.get('/make_bet/')
		request.user = self.user
		response = bet(request)

		self.assertEqual(response.status_code, 200)

	def test_make_accept_update_bet(self):
		game = Game.objects.all()[0]
		request = RequestFactory().post(
			"/make_bet/", {"game": game.gameId, "amount": 10})
		request.user = self.user
		request.session = {}

		response = make_bet(request)

		self.assertEqual(response.status_code, 200)

		acceptor = User.objects.create_user(username = 'lel', email = 'kekeke@keke.com', password = 'rofl')

		bet = GameBet.objects.all()[0]

		request = RequestFactory().post(
			"/accept_bet/"+str(bet.id)+"/", {"game": game.gameId, "amount": 10})
		request.user = acceptor

		response = accept_bet(request,bet.id)

		self.assertEqual(response.status_code, 302)

		updateBets()

if __name__ == '__main__':
		unittest.main()
