from rest_framework import serializers
from Admissions.models import AdmissionOpenClasses

class AdmissionOpenClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdmissionOpenClasses
        fields = "__all__"