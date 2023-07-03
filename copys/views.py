from rest_framework.views import APIView, status, Response
from .models import Copy
from .serializers import CopySerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics

class CopyView(generics.ListCreateAPIView):
        
    queryset= Copy.objects.all()
    serializer_class= CopySerializer

class CopyDetailView(generics.RetrieveUpdateAPIView):

    queryset= Copy.objects.all()
    serializer_class= CopySerializer

