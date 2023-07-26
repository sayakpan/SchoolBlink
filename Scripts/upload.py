import os
import django
import csv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SchoolData.settings")
django.setup()

from Profiles.models import *

data_path = "data.csv"

with open(data_path, "r") as data:
    csv_reader = csv.DictReader(data)

    for row in csv_reader:
        obj = School_Profiles()

        print(row["school_name"] + " - Uploading...")
        obj.school_name = row["school_name"]
        obj.email = row["email"]
        obj.number = row["number"]
        obj.address = row["address"]
        try:
            obj.country = Country.objects.get(country_name=row["country"])
            obj.state = State.objects.get(state_name=row["state"])
            obj.city = City.objects.get(city_name=row["city"])
            obj.save()
            print(row["school_name"] + "Uploaded Successfully!")
        except:
            print("Data Mismatch")
            pass
