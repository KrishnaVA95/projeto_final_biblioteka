from django.forms import model_to_dict
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from copys.models import Copy

from copys.serializers import CopySerializer
from .models import Loan
from django.utils import timezone
from workalendar.america import Brazil

class LoanSerializer(serializers.ModelSerializer):
    #copies= CopySerializer(many=True)
    loan_copies = serializers.SerializerMethodField()
    def get_loan_copies(self, values):
        copies_loan = CopySerializer(values.copies.all(), many=True)
        return copies_loan.data
    class Meta:
        model = Loan
        fields = ['id','overdue', 'created_at', 'deadline', 'finalized_loan', 'copies', 'account', 'loan_copies']
        read_only_fields = ['id', 'created_at', 'deadline', 'overdue', 'loan_copies' ]
        extra_kwargs ={'copies':{'write_only':True}}
 
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
        return super().create(validated_data) 
    


