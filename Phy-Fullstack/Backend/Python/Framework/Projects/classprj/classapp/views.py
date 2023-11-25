from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
from .models import Employee

# Create your views here.
class EmployeeCreate(CreateView):
    model=Employee
    template_name='employee_form.html'
    fields='__all__'
    success_url='/list'
class EmployeeList(ListView):
    model=Employee
    template_name='employee_list.html'
    def get_queryset(self):
        qs=Employee.objects.all()
        return qs 
class EmployeeDetails(DetailView):
    model=Employee
    template_name='employee_details.html'

class EmployeeUpdate(UpdateView):
    model=Employee
    template_name='employee_form.html'    
    fields='__all__'
    success_url='/list'

class EmployeeDelete(DeleteView):
    model=Employee 
    template_name='employee_form.html'   
    success_url='/list'
