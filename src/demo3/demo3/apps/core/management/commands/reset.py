from django.core.management.base import BaseCommand

from apps.core.models import Film


class Command(BaseCommand):
    help = 'Delete all Films'

    def handle(self, *args, **options):
        films = Film.objects.all()
        for film in films:
            film.delete()
