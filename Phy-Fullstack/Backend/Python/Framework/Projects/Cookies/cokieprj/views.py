from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# how to create our own cokkies
def setcookie(request):
    res=HttpResponse('Created our own cookies')
    res.set_cookie('name','Theju')
    return res
#set_cookie is default function
def getcookie(request):
    res=request.COOKIES.get('name')
    return HttpResponse(res)
def delcookie(request):
    res=HttpResponse('Deleted Cookie')
    res.delete_cookie('name')
    return res

   