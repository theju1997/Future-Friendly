from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_no=models.IntegerField(primary_key=True)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    gender=models.CharField(max_length=1)
    hire_date=models.DateTimeField(max_length=20)