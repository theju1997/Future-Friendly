class calculator:
    def add(self,a,b,c=0,d=0):
        if d!=0:
            print('I am 4 parameters of addition',a+b+c+d)
        elif c!=0:
            print('I am 3 parameters of addition',a+b+c)
        else:
            print('I am 2 parameters of addition',a+b)
c=calculator()
c.add(10,20,30)

