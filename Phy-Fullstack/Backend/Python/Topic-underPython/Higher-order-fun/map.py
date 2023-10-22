z=[1,2,3,4,5]
def flower(a):
    return a*2
result=list(map(flower,z))
print(result)

#by using lambada
z=[1,2,3,4,5]
result=list(map(lambda a:a*2,z))
print(result)

