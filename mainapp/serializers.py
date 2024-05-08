
from dataclasses import fields

from pyexpat import model

from rest_framework.serializers import Serializer, ModelSerializer

from rest_framework import serializers

from .models import SponsorModel, StudentModel, StudentSponsor, UniversityModel

class SponsorSerializers(serializers.ModelSerializer): 
    class Meta:
        model = SponsorModel
        fields = '__all__'
        
class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = '__all__'
        
class StudentSponsorSerializers(serializers.ModelSerializer):
    class Meta:
        model = StudentSponsor
        fields = '__all__'

class UniversitySerializers(serializers.ModelSerializer):
    class Meta:
        model = UniversityModel
        fields = '__all__'
        