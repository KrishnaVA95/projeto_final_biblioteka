from .models import Loan
from .serializers import LoanSerializer
from rest_framework import generics

class LoanView(generics.ListCreateAPIView):
    # apenas staff ou admin
    queryset= Loan.objects.all()
    serializer_class= LoanSerializer

class LoanDetailView(generics.RetrieveAPIView):
    # apenas staff, admin ou user autenticado
    queryset= Loan.objects.all()
    serializer_class= LoanSerializer

class LoanDetailUpdateView(generics.UpdateAPIView):
    # apenas staff ou admin 
    queryset= Loan.objects.all()
    serializer_class= LoanSerializer
    ...

class LoanDetailDestroyView(generics.DestroyAPIView):
    # apenas staff ou admin 
    queryset= Loan.objects.all()
    serializer_class= LoanSerializer
    ...
