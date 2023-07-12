from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Account
from loans.serializers import LoanSerializer

class AccountSerializer(serializers.ModelSerializer):
    loans_user = serializers.SerializerMethodField()
    def get_loans_user(self, values):
        loans_user = LoanSerializer(values.loans.all(), many=True)
        return loans_user.data
    class Meta:
        model = Account
        fields = [
            "id",
            "cpf",
            "username",
            "password",
            "email",
            "is_staff",
            "address",
            "created_at",
            "permission_loan",
            "loans_user"
        ]
        extra_kwargs = {
            "email": {"validators": [UniqueValidator(queryset=Account.objects.all())]},
            "password": {"write_only": True},
            "loans": {"write_only": True}
        }
        read_only_fields = [
            'id',
            "created_at",
            "permission_loan",
            "loans_user",
        ]


    def create(self, validated_data):
        if validated_data.get("is_staff"):
            return Account.objects.create_superuser(**validated_data)

        return Account.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.set_password(instance.password)
        instance.save()
        return instance


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=127, write_only=True)
    password = serializers.CharField(max_length=127, write_only=True)
