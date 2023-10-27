num1='hello'
num2='theju'
print(num1+num2)
print(num1.__add__(num2))
print(str.__add__(num1,num2))
print('=======================')

#program to use + operator on our own class objects
class Book:
    def __init__(self,title,pages):
        self.title=title
        self.pages=pages
    def __add__(self,other):
        return self.pages+other.pages
    
b1=Book('wings of fire',250)
b2=Book('2 states',150)
print('total number of pages',b1+b2)
print('===============================')
#Example on less than and gt
class college:
    def __init__(self,Name,Marks):
        self.Name=Name
        self.Marks=Marks
    def __gt__(self,other):
        return self.Marks>other.Marks
    def __lt__(self,other):
        return self.Marks<other.Marks
theju=350
rachu=250
print('print theju',theju>rachu)
print('print rachu',theju<rachu)

    


    
    