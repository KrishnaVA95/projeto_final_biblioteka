from django.test import TestCase
from accounts.models import Account
from books.models import Book
from copys.models import Copy
from genres.models import Gender
from loans.models import Loan
from publishing_companies.models import PublishingCompany


class BookCopyRelationTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.group = Group.objects.create(scientific_name="Canis familiares")

        cls.pets = [
            Pet.objects.create(
                name=f"pet{i}", age=i, weight=12, sex="female", group=cls.group
            )
            for i in range(5)
        ]

    def test_if_a_group_can_have_many_pets(self):
        message = "Verifique se você setou corretamente o relacionamento 1:N entre Group e Pet."

        self.assertEqual(len(self.pets), self.group.pets.count(), message)

        for pet in self.pets:
            self.assertEqual(pet.group, self.group, message)

    def test_if_a_group_deletion_is_protected(self):
        message = "Verifique se você protegeu os pets de uma deleção de grupo associado a pets"

        with self.assertRaises(models.ProtectedError, msg=message):
            self.group.delete()