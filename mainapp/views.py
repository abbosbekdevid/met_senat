from django.shortcuts import render

from rest_framework import generics

from .models import SponsorModel, StudentModel, StudentSponsor, UniversityModel

from .serializers import SponsorSerializers, StudentSerializers, UniversitySerializers, StudentSponsorSerializers

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.views import APIView, Response

# Create your views here.
    
    
class AllCreateSponsorView(generics.ListCreateAPIView):
    queryset = SponsorModel.objects.all()
    serializer_class = SponsorSerializers
    
    # http_method_names = ['patch', 'put', 'get']
    
class RUDSponsorView(generics.RetrieveUpdateAPIView):
    queryset = SponsorModel.objects.all()
    serializer_class = SponsorSerializers
    
class AllCreateStudentView(generics.ListCreateAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializers
    filter_backends = [DjangoFilterBackend,]
    filterset_fields = ('student_type')
    
class RUDStudentView(generics.RetrieveUpdateAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializers
    
class AllCreateUniversityView(generics.ListCreateAPIView):
    queryset = UniversityModel.objects.all()
    serializer_class = UniversitySerializers
    
class RUDUniversityView(generics.RetrieveUpdateAPIView):
    queryset = UniversityModel.objects.all()
    serializer_class = UniversitySerializers
    
    
class AllCreateStudentSponsorView(generics.ListCreateAPIView):
    queryset = StudentSponsor.objects.all()
    serializer_class = StudentSponsorSerializers
    
class RUDStudentSponsorView(generics.RetrieveUpdateAPIView):
    queryset = StudentSponsor.objects.all()
    serializer_class = StudentSponsorSerializers
    
    
    
class StatisticAPIView(APIView):
    
    
    def get(self, request):
        from django.db.models import Sum
        a = StudentSponsor.objects.aggregate(total=Sum('amount'))['total'] or 0
        t = StudentModel.objects.aggregate(total=Sum('contract'))['total'] or 0
        k = t-a
        
        return Response(data={'a':a, 't':t, 'k':k})