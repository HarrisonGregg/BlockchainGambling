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
