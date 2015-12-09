from .views import signin
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser, User

class TestSigninMethods(TestCase):

	def setUp(self):
		# Every test needs access to the request factory. 
		self.factory = RequestFactory()
		self.user = User.objects.create_user(
			username = 'haiwei', email = 'haiwei@...', password = 'top_secret')

	def test_details(self):
		# Create a instance of a GET request. 
		request = self.factory.get('/customer/details')

		request.user = AnonymousUser()

		# Test views as if it were dpeloyed at /customer/details

		response = views(request)
		# Use this syntax for class-based views. 
		response = views.as_view()(request)
		self.assertEqual(response.status_code, 200)

	


 #    def test_sign_in(self):
	#     """POST sets 'locale' key in session."""
	#     request = RequestFactory().post(
	#         "/sigin/", {"username": "", "password": ""})
	#     request.session = {}

	#     signin(request)

	#     self.assertEqual(
	#         request.session["signin"], "username", "password"

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
