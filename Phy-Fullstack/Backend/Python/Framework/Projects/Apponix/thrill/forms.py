from django import forms

from django.db import models

class ReviewForm(forms.Form):
    name = forms.CharField(max_length=20)
    email = forms.EmailField()
    ratings = forms.IntegerField()
    feedback = forms.CharField(widget=forms.Textarea)

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='uploaded_images/')    