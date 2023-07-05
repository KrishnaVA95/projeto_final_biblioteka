from django.test import TestCase
from loans.models import Loan

class LoanModelTest(TestCase):
    def test_created_at_properties(self):
        result = Loan._meta.get_field("created_at").auto_now_add
        msg = f"Verifique se a propriedade `auto_now_add` de `created_at` foi definida"
        self.assertTrue(result, msg)
    
    def test_deadline_properties(self):
        result = Loan._meta.get_field("deadline").auto_now_add
        msg = f"Verifique se a propriedade `auto_now_add` de `deadline` foi definida"
        self.assertTrue(result, msg)

    def test_overdue_properties(self):
        result = Loan._meta.get_field("overdue").default
        msg = f"Verifique se o valor padrão de `overdue` foi definido como `False`"
        self.assertFalse(result, msg)