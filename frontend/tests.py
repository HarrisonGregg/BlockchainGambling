from .views import signin
from django.test import TestCase, RequestFactory

class TestSigninMethods(TestCase):


    def test_sign_in(self):
	    """POST sets 'locale' key in session."""
	    request = RequestFactory().post(
	        "/sigin/", {"username": "", "password": ""})
	    request.session = {}

	    signin(request)

	    self.assertEqual(
	        request.session["signin"], "username", "password"

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
