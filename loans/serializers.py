from rest_framework import serializers
from .models import Loan
from django.utils import timezone
from workalendar.america import Brazil

class LoanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Loan
        fields = ['id','overdue', 'created_at', 'deadline']
        read_only_fields = ['id', 'created_at', 'deadline', 'overdue' ]

    def create(self, validated_data):
        # Define a data atual
        current_date = timezone.now().date()

        # Define o calendário brasileiro
        cal = Brazil()

        # Adiciona 5 dias úteis à data atual
        deadline = cal.add_working_days(current_date, 5)
        print(deadline)
        # Adiciona o prazo ao objeto Loan
        validated_data['deadline'] = deadline

        return super().create(validated_data)
    

