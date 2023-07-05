from django.test import TestCase
from publishing_companies.models import PublishingCompany

class PublishingCompanyModelTest(TestCase):
    def test_name_properties(self):
        expected = 50
        result = PublishingCompany._meta.get_field("name").max_length
        msg = f"Verifique se a propriedade `max_length` de `name` foi definida como `{expected}`"
        self.assertEqual(expected, result, msg)

        result = PublishingCompany._meta.get_field("name").unique
        msg = f"Verifique se o atributo `name` foi definido como unico"
        self.assertTrue(result, msg)

        result = PublishingCompany._meta.get_field("name").null
        msg = f"Verifique se o atributo `name` foi definido como obrigatório"
        self.assertFalse(result, msg)