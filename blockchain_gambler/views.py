from django.http import Http404
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from django.template import RequestContext


# Create your views here.
from .models import User
def index(request):
    return HttpResponse("Welcome to BitBet!")

def signup(request):
    return render(request,'signup.html')

def signin(request):
    return render(request, 'signin.html', context_instance=RequestContext(request, {}))
