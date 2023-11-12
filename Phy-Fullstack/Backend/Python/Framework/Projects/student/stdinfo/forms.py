from django import forms

class StudentForm(forms.Form):
    name=forms.CharField(max_length=20)
    age=forms.IntegerField()
    Gender=forms.CharField(max_length=20)
    date=forms.DateField()

