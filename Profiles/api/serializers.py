from rest_framework import serializers
from Profiles.models import *

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = "__all__"


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"


class SchoolTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolType
        fields = "__all__"


class SchoolFormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolFormat
        fields = "__all__"


class SchoolBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolBoard
        fields = "__all__"


class SchoolClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolClass
        fields = "__all__"


class SchoolProfilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = School_Profiles
        fields = "__all__"


class SchoolFacilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolFacilities
        fields = "__all__"
