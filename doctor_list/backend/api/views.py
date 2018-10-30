from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PhysicianSerializer, PatientSerializer
from backend.models import Physicians, Patient

context = dict()

class PhysicianListView(APIView):
    def get_object(self):
        try:
            
            return Physicians.objects.all()
        except Physicians.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
   
    def get(self, request):
        all = [] 
        ret = self.get_object()
        for obj in ret:
            all.append("{}, {}".format(obj.last_name, obj.first_name))
      
        print(all)
        context['doc_list'] = all
        return Response(context, status=status.HTTP_200_OK)

class PatientListView(APIView):
    def get_object(self, doctor):
        try:
            return Patient.objects.filter(doctor=doctor)
        except Patient.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        all = []
        ret = self.get_object(pk)
        for obj in ret:
            all.append("{} {} {} {}".format(obj.name, obj.date, obj.time, obj.kind))
        
        context['patient_list'] = all
        return Response(context, status=status.HTTP_200_OK) 
