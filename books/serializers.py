from rest_framework import serializers

from genres.models import Gender
from .models import Book, Publishing_company
from genres.serializer import GenderSerializer

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Publishing_company
        fields = ["id", "name"]   

class BookSerializer(serializers.ModelSerializer):
    genres = GenderSerializer(many=True)
    publishing_company = CompanySerializer()
    class Meta:
        model = Book
        fields = ["id","title","author","number_page","description","cover","published","number_copy","copies_available", "publishing_company", 'genres']

    def create(self, validated_data):
        gender_data = validated_data.pop("genres")
        publishing_company = validated_data.pop("publishing_company")

        publishing_company_obj = Publishing_company.objects.filter(name__iexact=publishing_company["name"]).first()

        if not publishing_company_obj:
            publishing_company_obj = Publishing_company.objects.create(**publishing_company)
        
        book = Book.objects.create(**validated_data, publishing_company=publishing_company_obj)

        for gender_dict in gender_data:
            try:
                gender_obj = Gender.objects.get(**gender_dict)
            except Gender.DoesNotExist:
                gender_obj = Gender.objects.create(**gender_dict)

            book.genres.add(gender_obj)

        return book
