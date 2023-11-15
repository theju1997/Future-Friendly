from django.shortcuts import render
from .forms import StudentForm 

# Create your views here.
def show(request):
    if request.method=='GET':
        form=StudentForm()
        return render(request,'index.html',{'form':form})
    else:
        form=StudentForm(request.POST)
        if form.is_valid:
            form.save(commit=True)
        return render(request,'img.html')