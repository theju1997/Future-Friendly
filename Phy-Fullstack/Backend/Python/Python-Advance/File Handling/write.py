#write
f=open('theju.txt','w')
f.write('I am developer \n')
f.write('I am a python developer')
f.close()

#write lines
f=open('theju.txt','w')
list1=['I am a theju \n','I like to do coding \n',]
f.writelines(list1)
f.close()

#with statement
with open('theju.txt','w')as f:
    f.write('Advantage of with statement')
    f.write('It will close the file automatically')

#Tell method  (used to check the curser point)  

with open('theju.txt','w')as x:
    print(x.tell())
    x.write('teju avinash rachana shankar')
    print(x.tell())
    
#seek method?(used to move the curser point to required place)
with open('theju.txt','r+')as y:
    print(y.tell())
    y.read()
    y.seek(5)
    print(y.tell())
    print(y.read())
    y.seek(0)
    print(y.tell())

