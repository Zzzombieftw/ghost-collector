from django.db import models

# Create your models here.
class Ghost(models.Model):
    name = models.CharField( max_length=50)
    decription = models.CharField(max_length=50)
    age = models.IntegerField()