from django.contrib import admin
from .models import League,BetData,User,GameBet
# Register your models here.
admin.site.register(League)
admin.site.register(BetData)
admin.site.register(GameBet)
# admin.site.register(User)