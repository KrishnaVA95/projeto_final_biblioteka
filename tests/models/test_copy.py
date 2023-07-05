from django.test import TestCase
from copys.models import Copy

class CopyModelTest(TestCase):
    def test_number_copy_book_properties(self):
        result = Copy._meta.get_field("number_copy_book").null
        msg = f"Verifique se o atributo `number_copy_book` foi definido como obrigatório"
        self.assertFalse(result, msg)

    def test_available_properties(self):
        result = Copy._meta.get_field("available").default
        msg = f"Verifique se o valor padrão de `available` foi definido como `True`"
        self.assertTrue(result, msg)

    def test_conservation_state_properties(self):
        expected = 100
        result = Copy._meta.get_field("conservation_state").max_length
        msg = f"Verifique se a propriedade `max_length` de `conservation_state` foi definida como `{expected}`"
        self.assertEqual(expected, result, msg)

        result = Copy._meta.get_field("conservation_state").null
        msg = f"Verifique se o atributo `conservation_state` foi definido como obrigatório"
        self.assertFalse(result, msg)