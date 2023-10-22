t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def find(x):
    return x % 2 == 0

result = list(filter(find, t))
print(result)

#by using lambda
t=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(filter(lambda x: x % 2 == 0, t))
print(result)

