import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

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

class Bet(models.Model):
	league = models.ForeignKey(League)
	user = models.ForeignKey(User)
	campaign = models.URLField()

	def __str__(self):
		return self.league.name + ":" + self.user.username

	campaign = models.TextField()
	result = models.TextField(default="")

class BetData(models.Model):
	username = models.CharField(max_length = 200)
	first_name = models.CharField(max_length = 30,null = False)
	last_name = models.CharField(max_length = 30,null = False)
	credit_number = models.CharField(max_length = 200,null = False)
	amount = models.DecimalField(max_digits=8,decimal_places=2)
	choice = models.CharField(max_length = 200)