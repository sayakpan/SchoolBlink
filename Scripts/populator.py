from django.conf import settings
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SchoolData.settings")
django.setup()

# Import the State model from the Profiles app
from Profiles.models import State,Country

state_list = ['Kerala', 'Madhyapradesh']

try:
    for state in state_list:
        obj = State()
        obj.state_name = state
        obj.country_name = Country.objects.all()[0]
        obj.save()

    print('Data Uploaded Successfully!')

except Exception as e:
    print('An error occurred:', str(e))

