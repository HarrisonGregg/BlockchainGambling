from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.contrib.auth.decorators import login_required
from .models import Team, Game
from datetime import datetime, date
from django.http import HttpResponse

# Create your views here.
def updateNBAteams():
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

def updateNBAgames(test=False):
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
					# Skip away games
					continue

				_other_team_url = columns[1].find_all('a')[1].attrs['href'].split('/')[-1]
				_other_team = Team.objects.get(prefix2=_other_team_url).name
				d = datetime.strptime(columns[0].text, '%a, %b %d')
				date = datetime(year, d.month, d.day)

				try:
					home_team_score,visit_team_score = columns[2].a.text.split(' ')[0].split('-')
					gameId = columns[2].a['href'].split('?id=')[1]
				except:
					home_team_score = None
					visit_team_score = None
					gameId = None

				try:
					game = Game.objects.get(date=datetime(year, d.month, d.day), home_team = _team, visit_team = _other_team)
				except:
					game = Game(
						date = date, 
						home_team = _team, 
						visit_team = _other_team
					)

				game.gameId = gameId
				game.home_team_score = home_team_score
				game.visit_team_score = visit_team_score

				game.save()

				if test:
					return HttpResponse("success!")

			except Exception as e:
				print(e)
	
	return HttpResponse("success!")
	