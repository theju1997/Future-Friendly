#This example for  Class, object, variable , self , reference variable
class student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno            #Constructor part
        self.marks=marks
    def result(self):
        print('my name is ',self.name)
        print('my rollno is ',self.rollno)          #method part
        print('my marks is ',self.marks)
        print('==========================')
s1=student('theju',57,85)
s1.result()
s2=student('Adi',58,85)
s2.result()


