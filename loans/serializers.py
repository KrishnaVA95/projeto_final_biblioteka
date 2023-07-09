from rest_framework import serializers
from .models import Loan
from django.utils import timezone
from workalendar.america import Brazil

class LoanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Loan
        fields = ['id','overdue', 'created_at', 'deadline', 'finalized_loan', 'copies', 'account']
        read_only_fields = ['id', 'created_at', 'deadline', 'overdue' ]

    def create(self, validated_data):
        # Define a data atual
        current_date = timezone.now().date()

        # Define o calendário brasileiro
        cal = Brazil()

        # Adiciona 3 dias úteis à data atual
        deadline = cal.add_working_days(current_date, 3)
        print(type( deadline ))
        # Adiciona o prazo ao objeto Loan
        validated_data['deadline'] = deadline
        # validated_data['deadline'] = '2023-07-08'

        return super().create(validated_data)
    


