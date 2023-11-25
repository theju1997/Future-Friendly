from django.db import models

# Create your models here.
class StudentData(models.Model):
    name=models.CharField(max_length=30)
    cname=models.CharField(max_length=30)
    email=models.EmailField(max_length=40)
    mobile=models.BigIntegerField()
    marks1=models.IntegerField()
    marks2=models.IntegerField()
    marks3=models.IntegerField()
