from django.shortcuts import render
from .form import StudentForm
from .models import student

# Create your views here.
def gonext(request):
    return render(request,'index.html')
def add(request):
    if request.method=='GET':
        form=StudentForm()
        return render(request,'index1.html',{'form':form})
    else:
        form=StudentForm(request.POST)
        if form.is_valid:
            form.save(commit=True)
        return render(request,'submitted.html')

        

    


