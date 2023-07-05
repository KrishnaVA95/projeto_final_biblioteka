from django.test import TestCase
from genres.models import Gender

class GenderModelTest(TestCase):
    def test_name_properties(self):
        expected = 127
        result = Gender._meta.get_field("name").max_length
        msg = f"Verifique se a propriedade `max_length` de `name` foi definida como `{expected}`"
        self.assertEqual(expected, result, msg)

        result = Gender._meta.get_field("name").unique
        msg = f"Verifique se o atributo `name` foi definido como unico"
        self.assertTrue(result, msg)

        result = Gender._meta.get_field("name").null
        msg = f"Verifique se o atributo `name` foi definido como obrigatório"
        self.assertFalse(result, msg)