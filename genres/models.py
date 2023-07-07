from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=30, unique=True)

    # books = models.ManyToManyField(
    #     "books.Book",
    #     on_delete=models.PROTECT,
    #     related_name="genres"
    # )

    def __repr__(self) -> str:
            return f"<Genre ({self.id})  |  {self.name})>"