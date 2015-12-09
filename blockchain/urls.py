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
    url(r'^make_bet/$', 'frontend.views.make_bet', name='make_bet'),
    url(r'^start/$', 'frontend.views.make_bet', name='make_bet'),
    url(r'^signup/$', 'frontend.views.signup', name='signup'),
    url(r'^bet/$', 'frontend.views.bet', name='bet'),
    url(r'^accept_bet/(?P<bet_id>.*)/$', 'frontend.views.accept_bet', name='accept_bet'),
    url(r'^logout/$', 'frontend.views.logout_view', name='logout'),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^updateNBAteams/$', 'scraper.views.updateNBAteams', name='updateNBAteams'),
    # url(r'^updateNBAgames/$', 'scraper.views.updateNBAgames', name='updateNBAgames'),
    # url(r'^updateBets/$', 'frontend.views.updateBets', name='updateBets'),
    # url(r'^join/$', 'frontend.views.join', name='join'),
    # url(r'^join/(?P<league_name>.*)/$', 'frontend.views.joinLeague', name='joinLeague'),
    # url(r'^manage/(?P<league_id>.*)/$','frontend.views.manage',name='manage'),
    # url(r'', include('blockchain_gambler.urls')),
]
