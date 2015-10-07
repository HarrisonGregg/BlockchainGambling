from .views import signin
from django.test import TestCase

class TestSigninMethods(TestCase):

  def test_nullsername(self):
      username = ""
      password = "123456"
      self.assertTrue(username == "")
      self.assertTrue(password =="123456")

  def test_nullpassword(self):
      username = "Haiwei Su"
      password = ""
      self.assertTrue(username == "Haiwei Su")
      self.assertTrue(password == "")

  def test_null(self):
      username = ""
      password = ""
      self.assertTrue(username == "")
      self.assertTrue(password == "")





if __name__ == '__main__':
    unittest.main()
