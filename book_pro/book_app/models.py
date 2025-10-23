from django.db import models
class Book(models.Model):
    book = models.CharField(max_length=100)
    authour = models.CharField(max_length=50)

 