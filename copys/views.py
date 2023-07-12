from rest_framework.views import APIView, status, Response
from .models import Copy
from .serializers import CopySerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics
from books.models import Book
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsUserStaff, IsUserStaffOrAuth
from rest_framework_simplejwt.authentication import JWTAuthentication

class CopyCreateView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserStaff]
        
    queryset= Copy.objects.all()
    serializer_class= CopySerializer

    def perform_create(self, serializer):
        book_id = self.kwargs['pk']
        book = get_object_or_404(Book, id=book_id)
        serializer.save(book=book)


class CopyListView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset= Copy.objects.all()
    serializer_class= CopySerializer
    

class CopyDetailView(generics.RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserStaffOrAuth]

    queryset= Copy.objects.all()
    serializer_class= CopySerializer

