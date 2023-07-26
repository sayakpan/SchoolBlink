import os
import django
import sys
import csv

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SchoolData.settings")
django.setup()

from Profiles.models import *

with open("school.csv", "r") as file:
    data = csv.DictReader(file)

    for row in data:
        schoolObj = School_Profiles()

        try:
            print(row["school_name"] + " - Uploading...")
            schoolObj.school_name = row["school_name"]
            schoolObj.email = row["email"]
            schoolObj.number = row["number"]
            schoolObj.address = row["address"]
            schoolObj.city_id = City.objects.get(city_name=row["city_name"])
            schoolObj.state_id = State.objects.get(state_name=row["state_name"])
            schoolObj.country_id = Country.objects.get(country_name=row["country_name"])
            schoolObj.save()
            print(row["school_name"] + " - DONE")
        except:
            print(row["school_name"] + " - Failed !!")
            pass
