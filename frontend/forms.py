from django import forms

class SigninForm(forms.Form):
    username = forms.CharField()
    # password = forms.PasswordField()


class SignupForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    # password = forms.PasswordField()
    # password2 = forms.PasswordField()