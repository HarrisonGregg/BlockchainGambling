"""blockchain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'frontend.views.signin', name='signin'),
    url(r'^start/$', 'frontend.views.start', name='start'),
    url(r'^updateNBAteams/$', 'scraper.views.updateNBAteams', name='updateNBAteams'),
    url(r'^updateNBAgames/$', 'scraper.views.updateNBAgames', name='updateNBAgames'),
    url(r'^signup/$', 'frontend.views.signup', name='signup'),
    url(r'^join/$', 'frontend.views.join', name='join'),
    url(r'^join/(?P<league_name>.*)/$', 'frontend.views.joinLeague', name='joinLeague'),
    url(r'^bet/$', 'frontend.views.bet', name='bet'),
    url(r'^accept_bet/(?P<bet_id>.*)/$', 'frontend.views.accept_bet', name='accept_bet'),
    url(r'^add_card/$', 'frontend.views.add_card', name='add_card'),
    url(r'^logout/$', 'frontend.views.logout_view', name='logout'),
    url(r'^result/$','frontend.views.result',name='result'),
    url(r'^result/(?P<bet_id>.*)/$','frontend.views.betResult',name='betResult'),
    url(r'^manage/(?P<league_id>.*)/$','frontend.views.manage',name='manage'),
    url(r'^congrats/$','frontend.views.congrats',name='congrats'),
    #url(r'', include('blockchain_gambler.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
