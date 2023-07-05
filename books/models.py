from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=127)
    author = models.CharField(max_length=127)
    number_page = models.IntegerField(validators=[min(4)])
    description = models.TextField()
    cover = models.CharField(max_length=255)
    published = models.IntegerField(validators=[min(4)])
    number_copy = models.IntegerField(validators=[min(4)])
    copies_available = models.IntegerField(validators=[min(2)])



