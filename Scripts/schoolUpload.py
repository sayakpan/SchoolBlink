import os
import django
import sys
import csv

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SchoolBlink.settings")
django.setup()

from Profiles.models import *

with open("SchoolUpload.csv", "r") as file:
    data = csv.DictReader(file)
    
    for row in data:
        schoolObj = School_Profiles()

        try:
            schoolObj.user=User.objects.get(id=row["user"])
            schoolObj.school_name = row["school_name"]
            schoolObj.email = row["email"]
            schoolObj.website = row["website"]
            schoolObj.number = row["number"]
            schoolObj.address = row["address"]

            schoolObj.school_format = SchoolFormat.objects.get(id=row["school_format"])
            schoolObj.school_type = SchoolType.objects.get(id=row["school_type"])
            
            schoolObj.school_timings = row["school_timings"]
            schoolObj.year_established = row["year_established"]
            schoolObj.latitude = row["latitude"]
            schoolObj.longitude = row["longitude"]
            schoolObj.about = row["about"]
            schoolObj.city = City.objects.get(city_name=row["city"])
            schoolObj.state = State.objects.get(state_name=row["state"])
            schoolObj.country = Country.objects.get(country_name=row["country"])
            schoolObj.save()

            # Many-to-many fields
           
            schoolObj.school_board.set([int(board_id) for board_id in row["school_board"].split(",")])
            schoolObj.school_class.set([int(class_id) for class_id in row["school_class"].split(",")])

            # Choice charfields
            schoolObj.coed_status = row["coed_status"]
            schoolObj.school_medium = row["school_medium"]
            schoolObj.ownership = row["ownership"]

            schoolObj.save()
            print(row["school_name"] + " - DONE")
        except:
            print(row["school_name"] + " - Failed !!")
            pass
