from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id","title","author","number_page","description","cover","published","number_copy","copies_available"]