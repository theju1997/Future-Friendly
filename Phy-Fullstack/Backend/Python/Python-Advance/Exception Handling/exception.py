#to handle zero division erro
a=int(input('Enter first number'))
b=int(input('Enter second number'))
try:
    c=a/b
    print(c)
except(ZeroDivisionError):
    print('Do notdivide by zero')
print('=============================')

#to handle value error
a=int(input('Enter first number'))
b=(input('Enter second number'))#dont give int
try:
    x=int(a)
    y=int(b)
    c=x/y
    print(c)
except(ZeroDivisionError):
    print('Do notdivide by zero')
except(ValueError):
    print('Do not enter alphabates')
print('=============================')

#Index error
try:
    mylist=["a","b","c","d"]
    id=int(input("Enter Id(1-4)"))
    print("Your name is",mylist[id-1],"and your id is ",id)
except(ValueError):
    print("do not enter string")
except(IndexError):
    print('Index out of range')

 #Default exept error
try:
    mylist=["a","b","c","d"]
    id=int(input("Enter Id(1-4)"))
    print("Your name is",mylist[id-1],"and your id is ",id)
except(ValueError):
    print("do not enter string")
except(IndexError):
    print('Index out of range')

  #finally
a=int(input('Enter first number'))
b=(input('Enter second number'))#dont give int
try:
    x=int(a)
    y=int(b)
    c=x/y
    print(c)
except(ZeroDivisionError):
    print('Do not divide by zero')
except(ValueError):
    print('Do not enter string')
finally:
    print('I am always executing')
print('=============================')


    
