import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

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
