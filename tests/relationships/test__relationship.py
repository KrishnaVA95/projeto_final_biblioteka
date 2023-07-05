from django.test import TestCase
from accounts.models import Account
from books.models import Book
from copys.models import Copy
from genres.models import Gender
from loans.models import Loan
from publishing_companies.models import PublishingCompany
from django.db import models


class PublishingCompanyBookRelationTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.publishing_company = PublishingCompany.objects.create(name="Martins fonts")

        cls.books = [
            Book.objects.create(
                title=f"book{i}", author=JRR Tolkien, number_page= 1200, description="Uma aventura fantástica pela terra-média", cover="https://tudosobreprodutos.com.br/img/livro-senhor-dos-aneis-o-capa-do-filme.png", published=2001, number_copy=5, copies_available=5, publishing_company=cls.publishing_company
            )
            for i in range(5)
        ]



class BookCopyRelationTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.book = Book.objects.create(title="O senhor dos anéis")

        cls.copys = [
            Copy.objects.create(
                number_copy_book=i, available=True, conservation_state="em bom estado", book=cls.book
            )
            for i in range(5)
        ]

    def test_if_a_book_can_have_many_copys(self):
        message = "Verifique se você setou corretamente o relacionamento 1:N entre Book e Copy."

        self.assertEqual(len(self.copys), self.book.copys.count(), message)

        for copy in self.copys:
            self.assertEqual(copy.book, self.book, message)

    def test_if_a_book_deletion_is_protected(self):
        message = "Verifique se você protegeu as copys de uma deleção de book associado a copy"

        with self.assertRaises(models.ProtectedError, msg=message):
            self.book.delete()