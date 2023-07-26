import django
import os
import csv
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SchoolData.settings")
django.setup()

from Profiles.models import *

with open("states.csv", "r") as file:
    data = csv.DictReader(file)

    for row in data:
        stateObj = State()
        try:
            print(row["state_name"] + " - Uploading...")
            stateObj.state_name = row["state_name"]
            stateObj.country_id = Country.objects.get(id=row["country_id"])
            stateObj.save()
            print(row["state_name"] + " - Done")

        except:
            pass
