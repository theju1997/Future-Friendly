#Example for class variable
class Employee:
    company_name='infosys'#class data
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal
print(Employee.company_name)
Employee.company_name='shivasys'
print(Employee.company_name)
e=Employee('Shankar',23000)
print(e.company_name)
teju=Employee('Shankar',23000)
print(teju.company_name)
teju.company_name='thejusys'
print(teju.company_name)
print(Employee.company_name)
print("=========================================")
#class method
class Employee:
    company_name='Infosys'
    def __init__(Self,name, salary):
        self.name=name
        self.salary=salary
    @classmethod             #In class method we should use this code 
    def display(cls):
        print(cls.company_name)
Employee.display()  



