import schedule
import time
from datetime import datetime
from loans.models import Loan

def check_loans():
    # Define a data atual
    current_date = datetime.now().date()

    # Percorre os objetos Loan
    for loan in Loan.objects.all():
        if loan.deadline <= current_date:
            loan.overdue = True
            loan.save()
            
    print( "CHEGAMOS NO PRINT",Loan.objects.all())   
    # Encerra a função após checar todos os livros
    # return


schedule_time = "18:30"

# Agende a função para ser executada todos os dias 
# schedule.every().day.at(schedule_time).do(check_loans)
schedule.every(60).seconds.do(check_loans)

while True:
    schedule.run_pending()
    time.sleep(1)
