from .models import Gender
from .serializer import GenderSerializer
from rest_framework import generics
from accounts.permissions import IsUserStaff
from rest_framework_simplejwt.authentication import JWTAuthentication

class GenderView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserStaff]
    queryset= Gender.objects.all()
    serializer_class= GenderSerializer


class GenderDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserStaff]
    queryset= Gender.objects.all()
    serializer_class= GenderSerializer
