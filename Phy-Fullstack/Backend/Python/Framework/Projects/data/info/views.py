from django.shortcuts import render
from .models import peoples
# Create your views here.
def display(request):
    if request.method=='GET':
        return render(request,'register.html')
    else:
        peoples(first_name = request.POST.get('first_name'),
                last_name = request.POST.get('last_name'),
                age =request.POST.get('age'),
                contacts =request.POST.get('contacts')).save()
                #email= request.POST.get('email')
                #pw= request.POST.get('pw')
    return render(request,'success.html')
