from django.core.management.base import BaseCommand, CommandError
from frontend.views import updateBets

class Command(BaseCommand):
	def handle(self, *args, **options):
		updateBets(None)
