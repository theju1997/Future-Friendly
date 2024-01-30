from django.shortcuts import render,redirect
from .models import StudentData


# Create your views here.
def nextpage(request):
    stdform=StudentData.objects.all()
    return render(request,'index.html',{'stdform':stdform})

def add_student(request):
    if request.method=='GET':
        return render(request,'studenform.html')
    else:
        StudentData(name=request.POST.get('name'),
                    cname=request.POST.get('cname'),
                    email=request.POST.get('email'),
                    mobile=request.POST.get('mobile'),
                    marks1=request.POST.get('marks1'),
                    marks2=request.POST.get('marks2'),
                    marks3=request.POST.get('marks3'),
                    ).save()
        stdform=StudentData.objects.all()
        return render(request,'index.html',{'stdform':stdform})

def update_data(request,id):
    student=StudentData.objects.get(id=id)
    return render(request,'updatedata.html',{'student':student})

def save_update_data(request,id):
    student=StudentData.objects.get(id=id)
    student.name=request.POST.get('name')
    student.cname=request.POST.get('cname')
    student.email=request.POST.get('email')
    student.mobile=request.POST.get('mobile')
    student.marks1=request.POST.get('marks1')
    student.marks2=request.POST.get('marks2')
    student.marks3=request.POST.get('marks3')    
    student.save()
    return redirect(nextpage)

def delete_data(request,id):
    student=StudentData.objects.get(id=id)
    student.delete()
    return redirect(nextpage)