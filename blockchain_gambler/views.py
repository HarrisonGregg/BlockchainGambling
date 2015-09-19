from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
# Create your views here.
from .models import User
def index(request):
    return HttpResponse("Welcome!")
