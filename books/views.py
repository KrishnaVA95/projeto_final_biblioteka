from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status
from rest_framework import generics
from books.models import Book, Publishing_company
from books.serializers import BookSerializer, CompanySerializer

class BookView(generics.ListCreateAPIView):
    queryset= Book.objects.all()
    serializer_class= BookSerializer


    def post(self, request: Request) -> Response:
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data,status.HTTP_201_CREATED)
       
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
     queryset= Book.objects.all()
     serializer_class= BookSerializer



class PublishCompanyView(generics.ListCreateAPIView):
    queryset= Publishing_company.objects.all()
    serializer_class= CompanySerializer
  
    def post(self, request:Request) -> Response:
        serializer = CompanySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)
    

class PublishCompanyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Publishing_company.objects.all()
    serializer_class= CompanySerializer    
