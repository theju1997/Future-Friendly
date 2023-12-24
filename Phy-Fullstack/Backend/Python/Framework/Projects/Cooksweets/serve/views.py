from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def create_session(request):
    request.session['Emp_name'] = 'Theju'
    request.session['Emp_Email'] = 'theju@gmail.com'
    return HttpResponse("<center><h1>Hii Every one <br><br> The Session is Set</h1></center>")

def access_session(request):
    response = "<h1>Welcome to Sessions of Lakshmi sir Student Portal</h1><br>"
    if request.session.get('Emp_name'):
        response += "Emp_Name : {0} <br>".format(request.session.get('Emp_name'))
    if request.session.get('Emp_Email'):
        response += "Emp_Email : {0} <br>".format(request.session.get('Emp_Email'))
        return HttpResponse(response)
    else:
        return redirect('create/')

def delete_session(request):
    try:
        del request.session['Emp_name']
        del request.session['Emp_Email']
    except KeyError:
        pass
    return HttpResponse("<h1>Sorry..Student<br>Session Data cleared</h1>")    
