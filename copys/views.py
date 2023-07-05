from rest_framework.views import APIView, status, Response
from .models import Copy
from .serializers import CopySerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics
from books.models import Book

class CopyView(generics.ListCreateAPIView):
        
    queryset= Copy.objects.all()
    serializer_class= CopySerializer

    def perform_create(self, serializer):
        book = get_object_or_404(Book)
        serializer.save(book=book)

class CopyDetailView(generics.RetrieveUpdateAPIView):

    queryset= Copy.objects.all()
    serializer_class= CopySerializer

