import csv
from django.core.management.base import BaseCommand
from Profiles.models import State, Country

class Command(BaseCommand):
    help = 'Populates the State model from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file to be processed')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        with open(csv_file, newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                state_name, country_name = row
                country = Country.objects.get(country_name=country_name)
                State.objects.create(state_name=state_name, country_id=country)
                self.stdout.write(self.style.SUCCESS(f'Successfully added state: {state_name}'))
