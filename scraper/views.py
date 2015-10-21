from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.contrib.auth.decorators import login_required
from .models import Team, Game, UpcomingGame
from datetime import datetime, date

from django.http import HttpResponse

# Create your views here.
@login_required(login_url='/')
def updateNBAteams(request):
	url = 'http://espn.go.com/nba/teams'
	r = requests.get(url)
	print(r)

	soup = BeautifulSoup(r.text, "html.parser")
	tables = soup.find_all('ul', class_='medium-logos')

	teams = []
	prefix_1 = []
	prefix_2 = []
	teams_urls = []
	for table in tables:
		lis = table.find_all('li')
		for li in lis:
			info = li.h5.a
			name = info.text
			url = info['href']
			team = Team(name=name)
			try:
				team = Team.objects.get(name=name)
			except:
				pass
			team.prefix1 = url.split('/')[-2]
			team.prefix2=url.split('/')[-1]
			team.url=url
			team.save()

	return HttpResponse("success!")

@login_required(login_url='/')
def updateNBAgames(request):
	year = 2015
	BASE_URL = 'http://espn.go.com/nba/team/schedule/_/name/{0}/{2}'

	for index, team in enumerate(Team.objects.all()):
		_team = team.name
		print(index)
		url = team.url
		r = requests.get(BASE_URL.format(team.prefix1, year, team.prefix2))
		table = BeautifulSoup(r.text, "html.parser").table
		for row in table.find_all('tr')[2:]: # Remove header
			columns = row.find_all('td')
			try:
				if columns[1].li.text != 'vs':
					continue
				_other_team = columns[1].find_all('a')[1].text
				print(_other_team)
				_score = [None,None]
				try:
					_score = columns[2].a.text.split(' ')[0].split('-')
				except:
					pass
				# _won = True if columns[2].span.text == 'W' else False

				d = datetime.strptime(columns[0].text, '%a, %b %d')

				try:
					id = columns[2].a['href'].split('?id=')[1]
				except:
					try:
						game = UpcomingGame.objects.get(date=datetime(year, d.month, d.day), home_team = _team, visit_team = _other_team)
					except:
						game = UpcomingGame(date=datetime(year, d.month, d.day), home_team = _team, visit_team = _other_team)
						game.save()
					continue

				game = Game(id=id)
				try:
					game = Game.objects.get(id=id)
				except:
					pass

				game.date = datetime(year, d.month, d.day)
				game.home_team = _team
				game.home_team_score = _score[0]
				game.visit_team = _other_team
				game.visit_team_score = _score[1]

				game.save()

			except Exception as e:
				# if str(e) == "'NoneType' object is not subscriptable":
				# 	raise e
				print(e)
			# except Exception as e:
			# 	print(e)
			# 	pass # Not all columns row are a match, is OK
				# print(e)
	
	return HttpResponse("success!")
	