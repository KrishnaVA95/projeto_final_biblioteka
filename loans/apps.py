from django.apps import AppConfig


class LoansConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'loans'
    
    # def ready(self) -> None:
    #     from loans.automation import check_loans
    #     check_loans.start()