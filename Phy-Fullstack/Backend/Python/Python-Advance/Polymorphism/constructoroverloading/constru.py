class calculator:
    def __init__(self,a):
        print('single parameter',a)
    def __init__(self,a,b):
        print('single parameter',a+b)
    def __init__(self,a,b,c):
        print('single parameter',a+b+c)
c=calculator(10,20,30)
c.add()

#some other types of easy way 
class Calculator:
    def __init__(self, a, b=0, c=0):
        print('Sum of parameters:', a + b + c)

c = Calculator(10, 20, 30)

