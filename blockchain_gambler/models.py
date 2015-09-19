import datetime
from django.utils import timezone
from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=200,blank = False,unique = True)
    password = models.CharField(max_length=200,blank = False)
    created_time = models.DateTimeField('created time',default = timezone.now())
    last_modified_time = models.DateTimeField('last modified time',default = timezone.now())
    email_addr = models.CharField(max_length=200,blank = False)
    def __str__(self):
        return self.user_name

