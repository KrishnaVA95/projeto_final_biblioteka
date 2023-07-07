from rest_framework.views import APIView, status, Response
from .models import Copy
from .serializers import CopySerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics
from books.models import Book

class CopyCreateView(generics.CreateAPIView):
        
    queryset= Copy.objects.all()
    serializer_class= CopySerializer

    def perform_create(self, serializer):
        book_id = self.kwargs['pk']
        book = get_object_or_404(Book, id=book_id)
        serializer.save(book=book)


class CopyListView(generics.ListAPIView):
    
    queryset= Copy.objects.all()
    serializer_class= CopySerializer
    

class CopyDetailView(generics.RetrieveUpdateAPIView):

    queryset= Copy.objects.all()
    serializer_class= CopySerializer

