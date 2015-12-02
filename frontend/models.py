import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from scraper.models import Game

class CreditCard(models.Model):
	user = models.OneToOneField(User)
	number = models.CharField(max_length = 200,null = False)

# Create your models here.
class League(models.Model):
	name = models.CharField(max_length=32, unique=True)
	admin = models.ForeignKey(User)
	fee = models.DecimalField(max_digits=5,decimal_places=2)

	def __str__(self):
		return self.name

class GameBet(models.Model):
	creator = models.ForeignKey(User, related_name='creator')
	acceptor = models.ForeignKey(User, related_name='acceptor',null=True,blank=True)
	game = models.ForeignKey(Game)
	winner = models.CharField(max_length=200,null=False)
	amount = models.IntegerField()
	completed = models.BooleanField(default=False)
	won = models.BooleanField(default=False)

	def __str__(self):
		other = [self.game.home_team,self.game.visit_team][int(self.winner == self.game.home_team)]
		return self.winner + " will defeat " + other 	

class Bet(models.Model):
	league = models.ForeignKey(League)

class BetData(models.Model):
	username = models.CharField(max_length = 200)
	first_name = models.CharField(max_length = 30,null = False)
	last_name = models.CharField(max_length = 30,null = False)
	credit_number = models.CharField(max_length = 200,null = False)
	amount = models.DecimalField(max_digits=8,decimal_places=2)
	choice = models.CharField(max_length = 200)