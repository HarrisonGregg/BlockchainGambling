from .views import signin
from django.test import TestCase

class TestSigninMethods(TestCase):


    def test_sign_in(self):
	    """POST sets 'locale' key in session."""
	    request = RequestFactory().post(
	        "/sigin/", {"username": "", "password": ""})
	    request.session = {}

	    signin(request)

	    self.assertEqual(
	        request.session["signin"], "username", "password"


if __name__ == '__main__':
		unittest.main()
