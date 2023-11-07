class TopTen:
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<=10:
            val=self.num
            self.num+=1
            return val
        else:
            raise StopIteration
values=TopTen()
it=iter(values)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print("================================")
#=============================================================
#Generator
def topten():
    yield 1
    yield 2

values=topten()
it=iter(values)
print(next(it))
print(next(it))
print("================================")
#Closure
#Inner function
def outerfunction():
    a=10
    def innerfunction():
        b=20
        print(a+b)
    innerfunction()
    print(a)

outerfunction()
print("================================")
#closure
def enter_number_outer():
    numbers=[]
    def enter_number_inner(x):
        numbers.append(x)
        print(numbers)
    return enter_number_inner

enter_num=enter_number_outer()
enter_num(3)
enter_num(4)
enter_num(7)
print("================================")
        