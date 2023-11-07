#Decorator example
def outer_div(func):
    def inner(x,y):
        if (x<y):
            x,y=y,x
        return func(x,y)
    return inner

@outer_div
def divide(x,y):
    print(x/y)
res=divide(30,40)
print(res)
print('============================')
#==============================
def deco(f):
    print('I am extra')
    f()
    print('I become as extra ordinary')


@deco
def darshan():
    print('I am ordinary')
print('============================')
#===============================
def Div_by_zero(func):
    def inner(x,y):
        if y==0:
            return "Quantity is zero"
        return func(x,y)
    return inner
@Div_by_zero
def Unitprice(Amount,Quantity):
    return Amount / Quantity
print(Unitprice(500,0))
print('============================')