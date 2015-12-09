from .views import signin, signup, bet, accept_bet
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

	def test_signup(self):
		request = self.factory.post('/signup/',{"username":"anon","password":"password","email":"anon@example.com"})

		response = signup(request)

		self.assertEqual(response.status_code, 302)

		user = authenticate(username="anon", password="password")

		self.assertIsNotNone(user)

	def test_sign_in(self):
		request = RequestFactory().post(
			"/signin/", {"username": "anon123", "password": "password"})
		request.session = {}

		response = signin(request)

		self.assertEqual(response.status_code, 200)

	# def test_bet(self):

	# 	request = self.factory.get('/bet/')
	# 	request.user = self.user
	# 	response = bet(request)

	# 	self.assertEqual(response.status_code, 200)

	# def test_accept_bet(self):
	# 	today = date.today()
	# 	game = Game(date=date, home_team=)
	# 	bet = GameBet(creator=self.user, game=game, amount=10, winner=game.home_team)

	# 	request = self.factory.post('/bet/',{"username":"anon","password":"password","email":"anon@example.com"})

	# 	response = signup(request)

	# 	self.assertEqual(response.status_code, 302)

	# 	user = authenticate(username="anon", password="password")

	# 	self.assertIsNotNone(user)


	# def test_details(self):
	# 	# Create a instance of a GET request. 
	# 	request = self.factory.get('/customer/details')

	# 	request.user = AnonymousUser()

	# 	# Test views as if it were deployed at /customer/details

	# 	response = views(request)
	# 	# Use this syntax for class-based views. 
	# 	response = views.as_view()(request)
	# 	self.assertEqual(response.status_code, 200)


	# def test_start(self):
	# 	"""POST sets 'locale' key in session."""
	#     request = RequestFactory().post(
	#         "/sigin/", {"username": "", "password": ""})
	#     request.session = {}

	#     signin(request)

	#     self.assertEqual(
	#         request.session["signin"], "username", "password"


if __name__ == '__main__':
		unittest.main()
