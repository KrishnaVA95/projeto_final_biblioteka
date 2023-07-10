from django.db import models

class Gender(models.Model):
    name = models.CharField(max_length=30)

    books = models.ManyToManyField(
        "books.Book",
        related_name="genres"
    )

    def __repr__(self) -> str:
            return f"<Genre ({self.id})  |  {self.name})>"