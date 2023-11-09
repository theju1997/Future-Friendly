from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def picture(request):
    # return HttpResponse('All actors are drama peoples')
    return render (request, 'login.html')
def picture1(request):
    return render (request,'movies.html')
