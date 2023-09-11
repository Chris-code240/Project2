from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=50,blank=False)
    

# Create your models here.
