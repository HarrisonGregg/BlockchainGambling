from django.core.management.base import BaseCommand, CommandError
from scraper.views import updateNBAgames

class Command(BaseCommand):
	def handle(self, *args, **options):
		updateNBAgames()
