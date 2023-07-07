from django.db import models

class Loan(models.Model):
    created_at = models.DateField(auto_now_add=True)
    deadline = models.DateField(null=True)
    overdue = models.BooleanField(null=True, default=False)

    copies = models.ManyToManyField(
        "copys.Copy",
        on_delete=models.PROTECT,
        related_name="loans"
    )

    account = models.ForeignKey(
        "accounts.Account",
        on_delete=models.PROTECT,
        related_name="loans",
    )

    def __repr__(self) -> str:
            return f"<Loan ({self.id}) {self.created_at} - {self.deadline} | Overdue: {self.overdue})>"
