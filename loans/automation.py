from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from loans.models import Loan
from accounts.models import Account

def check_loans():
    current_date = datetime.now().date()

    for loan in Loan.objects.all():
        if loan.finalized_loan == False:
            if loan.deadline <= current_date:
                loan.overdue = True
                Account.objects.filter(id=loan.account.id).update(permission_loan=False)
                loan.save()
    return


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_loans, 'interval', hours=24)
    # scheduler.add_job(check_loans, 'interval', seconds=10)
    scheduler.start()




