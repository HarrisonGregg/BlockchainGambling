from django.db import models

# Create your models here.
class Team(models.Model):
	name = models.CharField(max_length = 200,null = False)
	prefix1 = models.CharField(max_length = 20,null = False)
	prefix2 = models.CharField(max_length = 200,null = False)
	url = models.URLField()

	def __str__(self):
		return self.name

class Game(models.Model):
	gameId = models.IntegerField(null=True)
	date = models.DateField()
	home_team = models.CharField(max_length=200,null=False)
	home_team_score = models.IntegerField(null=True)
	visit_team = models.CharField(max_length=200,null=False)
	visit_team_score = models.IntegerField(null=True)
	
	def __str__(self):
		if self.gameId:
			return "{0}: {1} {2}, {3} {4}".format(self.date,self.home_team,self.home_team_score,self.visit_team,self.visit_team_score)
		return "{0}: {1} vs. {2}".format(self.date,self.home_team,self.visit_team)

# class UpcomingGame(models.Model):
# 	date = models.DateField()
# 	home_team = models.CharField(max_length=200,null=False)
# 	visit_team = models.CharField(max_length=200,null=False)

# 	def __str__(self):
# 		return str(self.date) + " " + self.home_team + " vs. " + self.visit_team
