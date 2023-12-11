
from django import forms
from .models import Catagory

class ReviewForm(forms.Form):
    name = forms.CharField(max_length=20)
    email = forms.EmailField()
    ratings = forms.IntegerField()
    feedback = forms.CharField(widget=forms.Textarea)

class CatagoryForm(forms.ModelForm):
    class Meta:
        model=Catagory
        fields='__all__'
 
