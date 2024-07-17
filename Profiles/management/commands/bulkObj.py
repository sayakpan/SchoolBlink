import csv
from django.core.management.base import BaseCommand
from Profiles.models import SchoolBoard

class Command(BaseCommand):
    help = 'Populates the model from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file to be processed')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        with open(csv_file, newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                obj_name = row
                SchoolBoard.objects.create(school_board=obj_name)
                self.stdout.write(self.style.SUCCESS(f'Successfully added: {obj_name}'))