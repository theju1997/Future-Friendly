import os
from django import apps
from django.shortcuts import render,redirect
from requests import request

from thrill.forms import ReviewForm, UploadedImage
from .models import CustomerData, ImageUploadForm



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

def gal(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            # Save the form data and create a new UploadedImage object
            image=form.cleaned_data['image']
            uploaded_image=UploadedImage(image=image)
            uploaded_image.save()
            return redirect('gal.html')  # Redirect to a page displaying the list of uploaded images
    else:
        form = ImageUploadForm()

    return render(request, 'gal.html', {'form': form})


def review(request):
    if request.method == 'GET':
        return render(request,'feed.html')
    else:
        CustomerData(name=request.POST.get('name'),
        email=request.POST.get('email'),
        ratings=request.POST.get('ratings'),
        feedback=request.POST.get('feedback')).save()

        #TO FETCH FEEDBACK DATA AGAIN AFTER SAVING
    data=CustomerData.objects.all() 
    return render(request, 'feed.html', {'data': data})

# def upload():
    


