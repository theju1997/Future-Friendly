from django.db import models

# Create your models here.
class peoples(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    contacts = models.IntegerField()
    #email= models.EmailField()
    #pw= models.CharField(max_length=30)
