from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status
from rest_framework import generics
from books.models import Book, Publishing_company
from books.serializers import BookSerializer, CompanySerializer


class BookView(generics.ListCreateAPIView):
    def get(self, request: Request) -> Response:
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        
        return Response(serializer.data, status.HTTP_200_OK)


    def post(self, request: Request) -> Response:
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data,status.HTTP_201_CREATED)
       
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
     queryset= Book.objects.all()
     serializer_class= BookSerializer



class PublishCompanyView(generics.ListCreateAPIView):
    def get(self, request: Request) -> Response:
        publish = Publishing_company.objects.all()
        serializer = BookSerializer(publish, many=True)
        
        return Response(serializer.data, status.HTTP_200_OK)   

    def post(self, request:Request) -> Response:
        serializer = CompanySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)
    

class PublishCompanyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Publishing_company.objects.all()
    serializer_class= CompanySerializer    
