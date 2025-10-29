from django.db import models
class Lib_manage(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=50)
    year=models.IntegerField()