class A:
    def A1(self):
        print('Phone')
class B:
    def B1(self):
        print('Money')
class C:
    def C1(self):
        print('Gold')
class D(A,B,C):
    def D1(self):
        print('Sliver')
class E(D):
    def E1(self):
        print('House')
class F(E):
    def F1(self):
        print('Laptop')
class G(F):
    def G1(self):
        print('Air')
class H(F):
    def H1(self):
        print('Water')
first=H()
first.H1()
first.F1()
first.E1()
first.D1()
first.A1()
first.B1()
first.C1()
print('==========')
second=G()
second.G1()
second.F1()
second.E1()
second.D1()
second.A1()
second.B1()
second.C1()
print('==========')
third=F()
third.F1()
third.E1()
third.D1()
third.A1()
third.B1()
third.C1()
print('==========')
fourth=E()
fourth.E1()
fourth.D1()
fourth.A1()
fourth.B1()
fourth.C1()
print('==========')
fifth=D()
fifth.D1()
fifth.A1()
fifth.B1()
fifth.C1()
print('==========')
six=C()
six.C1()
print('==========')
seven=B()
seven.B1()
print('==========')
eight=A()
eight.A1()
print('==========')









