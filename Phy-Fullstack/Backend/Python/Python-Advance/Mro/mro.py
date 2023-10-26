class A:
    pass
class B:
    pass
class C(A):
    pass
class D(B,C):
    pass
print(A.mro())
print(B.mro())
print(C.mro())
print(D.mro())