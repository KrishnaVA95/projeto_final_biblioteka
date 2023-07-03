from rest_framework.views import APIView, Request, Response, status
from .models import Loan
from django.shortcuts import get_object_or_404
from .serializers import LoanSerializer


class LoanView(APIView):
    def get(self, request: Request) -> Response:
        loans = Loan.objects.all()
        serializer = LoanSerializer(loans, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    def post(self, request: Request) -> Response:
        serializer = LoanSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
