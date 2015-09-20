import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User as DjangoUser

# Create your models here.
class League(models.Model):
	name = models.CharField(max_length=32, unique=True)

class User(DjangoUser):
	league = models.ForeignKey(League)
	campaign = models.TextField()

class BetData(models.Model):
	username = models.CharField(max_length = 200)
	first_name = models.CharField(max_length = 30,null = False)
	last_name = models.CharField(max_length = 30,null = False)
	credit_number = models.CharField(max_length = 200,null = False)
	amount = models.DecimalField(max_digits=8,decimal_places=2)
	choice = models.CharField(max_length = 200)