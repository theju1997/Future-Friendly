from django.http import HttpResponse
from django.shortcuts import render,redirect
from  .forms import CatagoryForm
from .models import Catagory , CustomerData



# Create your views here.
def appo(request):
    return render(request,'web.html')

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def serv(request):
    return render(request,'serv.html')

def contact(request):
    return render(request,'contact.html')

def feed(request):
    data=CustomerData.objects.all() 
    return render(request,'feed.html',{'data':data})

def image(request):
    return render(request,'gal.html')


def collection(request):
    if request.method == "POST":
        form = CatagoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, "success.html") 
    else:
        form=CatagoryForm()
        display_catgory = Catagory.objects.all()        
    return render(request,"collection.html", {'form':form,'data':display_catgory})

