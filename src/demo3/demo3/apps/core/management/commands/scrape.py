from django.core.management.base import BaseCommand

from apps.core.scrapers import (sexta3_scraper, sexta_scraper, nova_scraper,
                                nitro_scraper, neox_scraper, antena3_scraper)


class Command(BaseCommand):
    help = 'Scrapes all channels'

    def handle(self, *args, **options):
        sexta3_scraper.delay()
        sexta_scraper.delay()
        nova_scraper.delay()
        nitro_scraper.delay()
        neox_scraper.delay()
        antena3_scraper.delay()
