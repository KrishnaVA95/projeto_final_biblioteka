import schedule
import time
from datetime import datetime
from loans.models import Loan

def check_loans():
    print('TESTE DE AUTOMAÇÃO')
    # Define a data atual
    # current_date = datetime.now().date()
    # Percorre os objetos Loan
    # for loan in Loan.objects.all():
    #     if loan.deadline < current_date:
    #         loan.overdue = True
    #         loan.save()

# Define a hora do agendamento
schedule_time = "18:00"

# Agende a função para ser executada todos os dias 
# schedule.every().day.at(schedule_time).do(check_loans)

schedule.every(5).seconds.do(check_loans)

while True:
    schedule.run_pending()
    time.sleep(1)