from django.core.management import BaseCommand
from guests import csv_import


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('filename')

    def handle(self, *args, **options):
        filename = options['filename']
        csv_import.import_guests(filename)
