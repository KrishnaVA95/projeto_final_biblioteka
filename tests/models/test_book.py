from django.test import TestCase
from books.models import Book

class BookModelTest(TestCase):
    def test_title_properties(self):
        expected = 127
        result = Book._meta.get_field("title").max_length
        msg = f"Verifique se a propriedade `max_length` de `title` foi definida como `{expected}`"
        self.assertEqual(expected, result, msg)

        result = Book._meta.get_field("title").null
        msg = f"Verifique se o atributo `title` foi definido como obrigatório"
        self.assertFalse(result, msg)

    def test_author_properties(self):
        expected = 127
        result = Book._meta.get_field("author").max_length
        msg = f"Verifique se a propriedade `max_length` de `author` foi definida como `{expected}`"
        self.assertEqual(expected, result, msg)

        result = Book._meta.get_field("author").null
        msg = f"Verifique se o atributo `author` foi definido como obrigatório"
        self.assertFalse(result, msg)

    def test_number_page_properties(self):
        result = Book._meta.get_field("number_page").null
        msg = f"Verifique se o atributo `number_page` foi definido como obrigatório"
        self.assertFalse(result, msg)

    def test_description_properties(self):
        result = Book._meta.get_field("description").null
        msg = f"Verifique se o atributo `description` foi definido como obrigatório"
        self.assertFalse(result, msg)

    def test_cover_properties(self):
        expected = 255
        result = Book._meta.get_field("cover").max_length
        msg = f"Verifique se a propriedade `max_length` de `cover` foi definida como `{expected}`"
        self.assertEqual(expected, result, msg)

        result = Book._meta.get_field("cover").null
        msg = f"Verifique se o atributo `cover` foi definido como opcional"
        self.assertTrue(result, msg)

    def test_published_properties(self):
        result = Book._meta.get_field("published").null
        msg = f"Verifique se o atributo `published` foi definido como obrigatório"
        self.assertFalse(result, msg)   

    
    def test_number_copy_properties(self):
        result = Book._meta.get_field("number_copy").null
        msg = f"Verifique se o atributo `number_copy` foi definido como obrigatório"
        self.assertFalse(result, msg)

    def test_copies_available_properties(self):
        result = Book._meta.get_field("copies_available").null
        msg = f"Verifique se o atributo `copies_available` foi definido como obrigatório"
        self.assertFalse(result, msg)