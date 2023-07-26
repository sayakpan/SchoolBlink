import os
import django
import csv
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SchoolData.settings")
django.setup()

from Profiles.models import *

with open("city.csv", "r") as file:
    data = csv.DictReader(file)
    print("Uploading...")
    for row in data:
        cityObj = City()

        try:
            cityObj.city_name = row["city_name"]
            cityObj.state_id = State.objects.get(state_name=row["state_name"])
            cityObj.country_id = Country.objects.get(country_name=row["country_name"])
            cityObj.save()
            print(row["city_name"] + " - Done")

        except:
            print(row["city_name"] + " - Failed")
            pass
