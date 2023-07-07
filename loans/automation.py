from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from loans.models import Loan

def check_loans():
    current_date = datetime.now().date()

    for loan in Loan.objects.all():
        if loan.deadline <= current_date:
            loan.overdue = True
            loan.save()
    return


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_loans, 'interval', hours=24)
    scheduler.start()




