from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView

from Profiles.api.serializers import (
    CountrySerializer, StateSerializer, CitySerializer, 
    SchoolTypeSerializer, SchoolFormatSerializer, SchoolBoardSerializer,
    SchoolClassSerializer, SchoolProfilesSerializer, SchoolFacilitiesSerializer
)
from Profiles.models import (
    Country, State, City, 
    SchoolType, SchoolFormat, SchoolBoard,
    SchoolClass, School_Profiles, SchoolFacilities
)


class CountryListView(APIView):
    def get(self, request, format=None):
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data)


class StateListView(APIView):
    def get(self, request, format=None):
        states = State.objects.all()
        serializer = StateSerializer(states, many=True)
        return Response(serializer.data)


class CityListView(APIView):
    def get(self, request, format=None):
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data)


class SchoolTypeListView(APIView):
    def get(self, request, format=None):
        school_types = SchoolType.objects.all()
        serializer = SchoolTypeSerializer(school_types, many=True)
        return Response(serializer.data)


class SchoolFormatListView(APIView):
    def get(self, request, format=None):
        school_formats = SchoolFormat.objects.all()
        serializer = SchoolFormatSerializer(school_formats, many=True)
        return Response(serializer.data)


class SchoolBoardListView(APIView):
    def get(self, request, format=None):
        school_boards = SchoolBoard.objects.all()
        serializer = SchoolBoardSerializer(school_boards, many=True)
        return Response(serializer.data)


class SchoolClassListView(APIView):
    def get(self, request, format=None):
        classes = SchoolClass.objects.all()
        serializer = SchoolClassSerializer(classes, many=True)
        return Response(serializer.data)


class SchoolProfilesListView(APIView):
    def get(self, request, format=None):
        school_profiles = School_Profiles.objects.all()
        serializer = SchoolProfilesSerializer(school_profiles, many=True)
        return Response(serializer.data)


class SchoolFacilitiesListView(APIView):
    def get(self, request, format=None):
        facilities = SchoolFacilities.objects.all()
        serializer = SchoolFacilitiesSerializer(facilities, many=True)
        return Response(serializer.data)


# RetrieveAPIView
class SchoolProfileDetailView(RetrieveAPIView):
    queryset = School_Profiles.objects.all()
    serializer_class = SchoolProfilesSerializer
    lookup_field = 'slug'

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        facilities = SchoolFacilities.objects.filter(school=instance)
        serializer = self.serializer_class(instance)
        data = serializer.data
        data['facilities'] = SchoolFacilitiesSerializer(facilities, many=True).data
        return Response(data)