from rest_framework import serializers
from .models import Copy
from books.serializers import BookSerializer

class CopySerializer(serializers.ModelSerializer):
    book= BookSerializer(read_only=True)
    class Meta:
        ordering = ["id"]
        model = Copy
        fields = ["id", "number_copy_book", "available", "conservation_state", "book"]

    def create(self, validated_data):
        if validated_data['book'].number_copy >= validated_data['number_copy_book']:
            return super().create(validated_data)
        else:
            raise serializers.ValidationError("invalid copy number")