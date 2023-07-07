from rest_framework import serializers
from .models import Book, Publishing_company

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id","title","author","number_page","description","cover","published","number_copy","copies_available", "publishing_company_id", "users", 'genres']


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Publishing_company
        fields = ["id", "name"]       