from django.core.management.base import BaseCommand, CommandError
from scraper.views import updateNBAteams

class Command(BaseCommand):
	def handle(self, *args, **options):
		updateNBAteams()
