from django.shortcuts import get_object_or_404

from copys.models import Copy
from .models import Loan
from copys.models import Copy
from .serializers import LoanSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from rest_framework import serializers
from accounts.permissions import IsUserStaffOrAuth
from rest_framework_simplejwt.authentication import JWTAuthentication

class LoanView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserStaffOrAuth]
    queryset= Loan.objects.all()
    serializer_class= LoanSerializer

    def perform_create(self, serializer):
        copies = serializer.validated_data['copies']
        account = serializer.validated_data['account']
        if account.permission_loan == True:
            for copy in copies:
                if copy.available:
                    copy.available = False
                    copy.save()
                    book = copy.book
                    book.copies_available -= 1
                    book.save()
                else:
                    raise serializers.ValidationError("The copy is not available")
            serializer.save()
        else:
            raise serializers.ValidationError("User has outstanding delays")

class LoanDetailView(generics.RetrieveUpdateAPIView):
    # apenas staff, admin ou user autenticado
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserStaffOrAuth]
    queryset= Loan.objects.all()
    serializer_class= LoanSerializer

    def put(self, request, *args, **kwargs):
        try:
            loan = self.get_object()
        except Loan.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if loan.finalized_loan == False and request.data.get('finalized_loan') == True:
            with transaction.atomic():
                
                loan.finalized_loan = True
                loan.save()

                Copy.objects.filter(loans=loan.id).update(available=True)

                for key in request.data:
                    setattr(loan, key, request.data[key])
                loan.save()

                serializer = LoanSerializer(loan)

                copies = loan.copies.all()
                for copy in copies:
                    book = copy.book
                    book.copies_available += 1
                    book.save()

                return Response(serializer.data)