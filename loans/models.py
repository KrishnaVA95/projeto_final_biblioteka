from django.db import models

class Loan(models.Model):
    created_at = models.DateField(auto_now_add=True)
    deadline = models.DateField(null=True)
    overdue = models.BooleanField(null=True, default=False)


    def __repr__(self) -> str:
        return f"<Loan () )>"




