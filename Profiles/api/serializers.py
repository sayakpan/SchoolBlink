from rest_framework import serializers
from Profiles.models import *

class School_Profiles_Serializer(serializers.ModelSerializer):
    class Meta:
        model = School_Profiles
        fields = "__all__"