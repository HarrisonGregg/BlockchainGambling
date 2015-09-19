from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from django.template import RequestContext
from .forms import SigninForm, SignupForm

# Create your views here.

def signin(request):
	form = SigninForm()
	return render(request, 'frontend/signin.html', context_instance=RequestContext(request, {form: form}))

def signup(request):
	form = SignupForm()
	return render(request, 'frontend/signup.html', context_instance=RequestContext(request, {form: form}))
