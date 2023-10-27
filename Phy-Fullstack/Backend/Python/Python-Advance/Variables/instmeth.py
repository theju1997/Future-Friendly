class Employee:
    def __init__(self, name, id, sal):
        self.name=name
        self.id=id
        self.sal=sal
    
    def display(self):
        print("Name is :",self.name)
        print("Id is :",self.id)
        print("Salary is :",self.sal)
e=Employee("Theju",17,30000)
e.display()
        