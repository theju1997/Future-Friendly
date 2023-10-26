#Example for hierarchicle
class prince:
    def p1(self):
        print('bike')
class chandu(prince):
    def c1(self):
        print('BMW')
class chandini(prince):
    def c2(self):
        print('mini cooper')
cdu=chandu()
cdu.c1()
cdu.p1()
cdn=chandini()
cdn.c2()
cdn.p1()