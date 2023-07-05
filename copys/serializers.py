from rest_framework import serializers
from .models import Copy
from books.serializers import BookSerializer

class CopySerializer(serializers.ModelSerializer):
    book = BookSerializer
    class Meta:
        model = Copy
        fields = ["id", "number_copy_book", "available", "conservation_state", "book"]