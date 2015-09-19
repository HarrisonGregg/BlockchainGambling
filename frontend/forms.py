from django.forms import Form

class SigninForm(Form):
    username = CharField()
    password = PasswordField()


class SignupForm(Form):
    username = CharField()
    email = EmailField()
    password = PasswordField()
    password2 = PasswordField()