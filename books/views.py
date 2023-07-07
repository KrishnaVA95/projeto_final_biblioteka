from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status

from books.models import Book
from books.serializers import BookSerializer
from rest_framework import generics


class BookView(APIView):
    def get(self, request: Request) -> Response:
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
