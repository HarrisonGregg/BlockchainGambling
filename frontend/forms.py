from django import forms

class SigninForm(forms.Form):
	auto_id = False 
	username = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Username'}))
	password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class StartForm(forms.Form):
	auto_id = False
	name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'League Name'}))
	fee = forms.DecimalField(label="",decimal_places=2,widget=forms.NumberInput(attrs={'placeholder': 'Entree Fee', 'min': '0.01', 'step': '0.01'}))

class SignupForm(forms.Form):
	auto_id = False 
	username = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Username'}))
	email = forms.EmailField(label="", widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
	password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
	password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'Re-type Password'}))

class JoinForm(forms.Form):
	league_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'League Name'}))
	campaign = forms.URLField(label="", widget=forms.TextInput(attrs={'placeholder': 'GoFundMe Campaign URL'}))

class BetForm(forms.Form):
	auto_id = False 
	amount = forms.DecimalField(label="",decimal_places=2,widget=forms.NumberInput(attrs={'placeholder': 'Amount in USD', 'min': '0.01', 'step': '0.01'}))
	choice = forms.ChoiceField(label="", choices=[('Heads','heads'),('Tails','tails')])