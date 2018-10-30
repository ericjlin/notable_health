from rest_framework import serializers
from backend.models import Physicians, Patient
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
class PhysicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Physicians
        fields = '__all__'

@csrf_exempt
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
