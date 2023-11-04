import re
data='aa ab ac abc abbc acc'
pattern='ab*c'
result=re.findall(pattern,data)
print(result)