#get ESPN NBA games stats
#credited: http://danielfrg.com/blog/2013/04/01/nba-scraping-data/

import copper
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime, date
# copper.project.path = '../'

year = 2015
teams = pd.read_csv('teams.csv')
BASE_URL = 'http://espn.go.com/nba/team/schedule/_/name/{1}/{2}'

match_id = []
dates = []
home_team = []
home_team_score = []
visit_team = []
visit_team_score = []

for index, row in teams.iterrows():
    _team, url = row['team'], row['url']
    r = requests.get(BASE_URL.format(row['prefix_1'], year, row['prefix_2']))
    table = BeautifulSoup(r.text, "html.parser").table
    for row in table.find_all('tr')[1:]: # Remove header
        columns = row.find_all('td')
        try:
            _home = True if columns[1].li.text == 'vs' else False
            _other_team = columns[1].find_all('a')[1].text
            _score = columns[2].a.text.split(' ')[0].split('-')
            _won = True if columns[2].span.text == 'W' else False

            match_id.append(columns[2].a['href'].split('?id=')[1])
            home_team.append(_team if _home else _other_team)
            visit_team.append(_team if not _home else _other_team)
            d = datetime.strptime(columns[0].text, '%a, %b %d')
            dates.append(date(year, d.month, d.day))

            if _home:
                if _won:
                    home_team_score.append(_score[0])
                    visit_team_score.append(_score[1])
                else:
                    home_team_score.append(_score[1])
                    visit_team_score.append(_score[0])
            else:
                if _won:
                    home_team_score.append(_score[1])
                    visit_team_score.append(_score[0])
                else:
                    home_team_score.append(_score[0])
                    visit_team_score.append(_score[1])
        except Exception as e:
            pass # Not all columns row are a match, is OK
            # print(e)

dic = {'id': match_id, 'date': dates, 'home_team': home_team, 'visit_team': visit_team,
        'home_team_score': home_team_score, 'visit_team_score': visit_team_score}

games = pd.DataFrame(dic).drop_duplicates(subset='id').set_index('id')
print(games)
games.to_csv('games.csv')