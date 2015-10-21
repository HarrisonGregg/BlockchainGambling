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
	id = models.IntegerField(primary_key = True)
	date = models.DateField()
	home_team = models.ForeignKey(Team, related_name='home_team')
	home_team_score = models.IntegerField()
	visit_team = models.ForeignKey(Team, related_name='visit_team')
	visit_team_score = models.IntegerField()

	def __str__(self):
		return home_team.name + " vs. " + visit_team.name