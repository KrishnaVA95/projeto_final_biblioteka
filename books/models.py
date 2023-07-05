from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=127)
    author = models.CharField(max_length=127)
    number_page = models.IntegerField(max_length=4)
    description = models.TextField()
    cover = models.CharField(max_length=255)
    published = models.IntegerField(max_length=4)
    number_copy = models.IntegerField(max_length=2)
    copies_available = models.IntegerField(max_length=2)



