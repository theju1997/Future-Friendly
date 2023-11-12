from django.shortcuts import render
from .models import StudentData
from .forms import StudentForm
# Create your views here.
def display(request):
    if request.method=='GET':
        form=StudentForm()
        return render(request,'register.html',{'form':form})
    else:
        form=StudentForm(request.POST)
        if form.is_valid():
            StudentData(
                name=form.cleaned_data['name'],
                age=form.cleaned_data['age'],
                Gender=form.cleaned_data['Gender'],
                date=form.cleaned_data['date'],
            ).save()
        return render(request,'result1.html')
  
