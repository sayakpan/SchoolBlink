import os
import django
import sys
import csv

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SchoolBlink.settings")
django.setup()

from Profiles.models import *

with open("SchoolFacilities.csv", "r") as file:
    data = csv.DictReader(file)
    
    for row in data:
        schoolobj=School_Profiles.objects.get(id=row["school"])

        try:
            facilitiesObj = SchoolFacilities.objects.get(school=schoolobj)

            facilitiesObj.AC_Classes = row["AC_Classes"]
            facilitiesObj.Wifi = row["Wifi"]
            facilitiesObj.Smart_Classes = row["Smart_Classes"]
            facilitiesObj.Boys_Hostel = row["Boys_Hostel"]
            facilitiesObj.Girls_Hostel = row["Girls_Hostel"]
            facilitiesObj.Cafeteria = row["Cafeteria"]
            facilitiesObj.Library = row["Library"]
            facilitiesObj.Playground = row["Playground"]
            facilitiesObj.Auditorium = row["Auditorium"]
            facilitiesObj.CCTV = row["CCTV"]
            facilitiesObj.GPS_Bus_Tracking_App = row["GPS_Bus_Tracking_App"]
            facilitiesObj.Student_Tracking_App = row["Student_Tracking_App"]
            facilitiesObj.Alumni_Association = row["Alumni_Association"]
            facilitiesObj.Medical_Room = row["Medical_Room"]
            facilitiesObj.Day_care = row["Day_care"]
            facilitiesObj.Meals = row["Meals"]
            facilitiesObj.Transportation = row["Transportation"]
            facilitiesObj.Art_and_Craft = row["Art_and_Craft"]
            facilitiesObj.Dance = row["Dance"]
            facilitiesObj.Drama = row["Drama"]
            facilitiesObj.Music = row["Music"]
            facilitiesObj.Picnics_and_excursion = row["Picnics_and_excursion"]
            facilitiesObj.Debate = row["Debate"]
            facilitiesObj.Gardening = row["Gardening"]
            facilitiesObj.Indoor_Sports = row["Indoor_Sports"]
            facilitiesObj.Outdoor_Sports = row["Outdoor_Sports"]
            facilitiesObj.Karate = row["Karate"]
            facilitiesObj.Taekwondo = row["Taekwondo"]
            facilitiesObj.Yoga = row["Yoga"]
            facilitiesObj.Gym = row["Gym"]
            facilitiesObj.Swimming_Pool = row["Swimming_Pool"]
            facilitiesObj.Skating = row["Skating"]
            facilitiesObj.Horse_Riding = row["Horse_Riding"]
            facilitiesObj.Computer_Lab = row["Computer_Lab"]
            facilitiesObj.Science_Lab = row["Science_Lab"]
            facilitiesObj.Robotics_Lab = row["Robotics_Lab"]
            facilitiesObj.Ramps = row["Ramps"]
            facilitiesObj.Washrooms = row["Washrooms"]
            facilitiesObj.Elevators = row["Elevators"]
            facilitiesObj.save()

            print(schoolobj.school_name + " - Facilities UPDATED")
        except:
            print(schoolobj.school_name + " - Failed !!")
            pass
