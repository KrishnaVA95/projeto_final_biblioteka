from .models import Genre
from .serializer import GenreSerializer
from rest_framework import generics

class GenreView(generics.ListCreateAPIView):
    queryset= Genre.objects.all()
    serializer_class= GenreSerializer


class GenreDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Genre.objects.all()
    serializer_class= GenreSerializer
