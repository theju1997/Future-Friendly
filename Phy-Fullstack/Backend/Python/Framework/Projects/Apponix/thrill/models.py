from django import forms
from django.db import models

# Create your models here.
class CustomerData(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    ratings=models.IntegerField()
    feedback=models.TextField()

    
class ImageUploadForm(forms.Form):
    image = forms.ImageField()