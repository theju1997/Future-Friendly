# import functools
# a=[3,4,5,6,7]
# def add(x,y):
#     return(x+y)
# output=functools.reduce(add,a)
# print(output)

#By using lambda
import functools
a=[3,4,5,6,7]
output=functools.reduce(lambda x,y:x+y ,a)
print(output)

