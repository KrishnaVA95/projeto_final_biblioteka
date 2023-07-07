from .models import Gender
from .serializer import GenderSerializer
from rest_framework import generics

class GenderView(generics.ListCreateAPIView):
    queryset= Gender.objects.all()
    serializer_class= GenderSerializer


class GenderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Gender.objects.all()
    serializer_class= GenderSerializer
