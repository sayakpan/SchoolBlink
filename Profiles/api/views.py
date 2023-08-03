from rest_framework.response import Response
from rest_framework.views import APIView

from Profiles.api.serializers import School_Profiles_Serializer
from Profiles.models import School_Profiles

class SchoolProfilesListView(APIView):
    def get(self, request, format=None):
        schoolList=School_Profiles.objects.all()
        serializer=School_Profiles_Serializer(schoolList,many=True)
        return Response(serializer.data)