from django.test import TestCase
from accounts.models import Account

class UserModelTest(TestCase):
    def test_email_properties(self):
        expected = 127
        result = Account._meta.get_field("email").max_length
        msg = f"Verifique se a propriedade `max_length` de `email` foi definida como `{expected}`"
        self.assertEqual(expected, result, msg)

        result = Account._meta.get_field("email").unique
        msg = f"Verifique se o atributo `email` foi definido como unico"
        self.assertTrue(result, msg)

        result = Account._meta.get_field("email").null
        msg = f"Verifique se o atributo `email` foi definido como obrigatório"
        self.assertFalse(result, msg)

    def test_username_properties(self):
        expected = 127
        result = Account._meta.get_field("username").max_length
        msg = f"Verifique se a propriedade `max_length` de `username` foi definida como `{expected}`"
        self.assertEqual(expected, result, msg)

        result = Account._meta.get_field("username").null
        msg = f"Verifique se o atributo `username` foi definido como obrigatório"
        self.assertFalse(result, msg)

    def test_password_properties(self):
        expected = 128
        result = Account._meta.get_field("password").max_length
        msg = f"Verifique se a propriedade `max_length` de `password` foi definida como `{expected}`"
        self.assertEqual(expected, result, msg)

        result = Account._meta.get_field("password").null
        msg = f"Verifique se o atributo `password` foi definido como obrigatório"
        self.assertFalse(result, msg)

    def test_is_staff_properties(self):
        result = Account._meta.get_field("is_staff").default
        msg = f"Verifique se o valor padrão de `is_staff` foi definido como `False`"
        self.assertFalse(result, msg)

    def test_address_properties(self):
        expected = 255
        result = Account._meta.get_field("address").max_length
        msg = f"Verifique se a propriedade `max_length` de `address` foi definida como `{expected}`"
        self.assertEqual(expected, result, msg)

        result = Account._meta.get_field("address").null
        msg = f"Verifique se o atributo `address` foi definido como obrigatório"
        self.assertFalse(result, msg)

    def test_cpf_properties(self):
        expected = 11
        result = Account._meta.get_field("cpf").max_length
        msg = f"Verifique se a propriedade `max_length` de `cpf` foi definida como `{expected}`"
        self.assertEqual(expected, result, msg)

        result = Account._meta.get_field("cpf").null
        msg = f"Verifique se o atributo `cpf` foi definido como obrigatório"
        self.assertFalse(result, msg)   

    
    def test_created_at_properties(self):
        result = Account._meta.get_field("created_at").auto_now_add
        msg = f"Verifique se a propriedade `auto_now_add` de `created_at` foi definida"
        self.assertTrue(result, msg)

        result = Account._meta.get_field("created_at").null
        msg = f"Verifique se o atributo `created_at` foi definido como obrigatório"
        self.assertFalse(result, msg)

    def test_permission_loan_properties(self):
        result = Account._meta.get_field("permission_loan").default
        msg = f"Verifique se o valor padrão de `permission_loan` foi definido como `True`"
        self.assertTrue(result, msg)