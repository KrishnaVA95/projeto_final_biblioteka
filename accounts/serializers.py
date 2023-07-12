from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
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
            "loans"
        ]
        extra_kwargs = {
            "email": {"validators": [UniqueValidator(queryset=Account.objects.all())]},
            "password": {"write_only": True},
        }
        read_only_fields = [
            'id',
            "created_at",
            "permission_loan",
            "loans"
        ]


    def create(self, validated_data):
        if validated_data["is_staff"] == True:
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
