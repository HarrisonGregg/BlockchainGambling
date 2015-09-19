from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from django.template import RequestContext

# Create your views here.

def signin(request):
	return render(request, 'frontend/signin.html', context_instance=RequestContext(request, {}))
