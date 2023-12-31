from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=127)
    author = models.CharField(max_length=127)
    number_page = models.IntegerField()
    description = models.TextField()
    cover = models.CharField(max_length=255)
    published = models.IntegerField()
    number_copy = models.IntegerField()
    copies_available = models.IntegerField()
    publishing_company = models.ForeignKey(
        "books.Publishing_company",
        on_delete=models.PROTECT,
        related_name="books"
    )
    users = models.ManyToManyField(
        "accounts.Account", 
        related_name="books"
    )

class Publishing_company(models.Model):
    name = models.CharField(max_length=50)




