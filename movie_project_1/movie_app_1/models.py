from django.db import models

class Customer(models.Model):
    movie = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.movie} ({self.year})"
class Contact(models.Model):
    full_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=13)