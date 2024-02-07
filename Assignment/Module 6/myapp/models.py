from django.db import models

# Create your models here.
class BookModel(models.Model):
    title=models.CharField(max_length=30)
    author=models.CharField(max_length=30)
    isbn=models.BigIntegerField()
    publisher=models.CharField(max_length=40)
