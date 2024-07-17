from rest_framework import serializers
from Profiles.models import *

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['id', 'state_name']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['country'] = {
            'id': instance.country_id.id,
            'name': instance.country_id.country_name
        }
        return representation


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'city_name']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['state'] = {
            'id': instance.state_id.id,
            'name': instance.state_id.state_name
        }
        representation['country'] = {
            'id': instance.country_id.id,
            'name': instance.country_id.country_name
        }
        return representation


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
