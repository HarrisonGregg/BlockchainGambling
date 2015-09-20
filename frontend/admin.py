from django.contrib import admin
from .models import League,BetData,User
# Register your models here.
admin.site.register(League)
admin.site.register(BetData)
admin.site.register(User)