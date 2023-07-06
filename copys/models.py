from django.db import models

class Copy(models.Model):

    number_copy_book = models.IntegerField()
    available = models.BooleanField(default="True")
    conservation_state = models.CharField(max_length=100)

    book = models.ForeignKey("books.Book", on_delete=models.PROTECT, related_name="copies")
