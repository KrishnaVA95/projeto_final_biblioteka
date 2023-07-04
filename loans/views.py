from .models import Loan
from .serializers import LoanSerializer
from rest_framework import generics

class LoanView(generics.ListCreateAPIView):
    queryset= Loan.objects.all()
    serializer_class= LoanSerializer


class LoanDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Loan.objects.all()
    serializer_class= LoanSerializer
    