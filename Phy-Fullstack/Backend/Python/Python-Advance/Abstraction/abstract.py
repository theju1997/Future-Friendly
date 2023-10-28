#normal class (we can create object)
class theju:
    def m1(self):
        pass
t=theju()
print(t)
print('================================')
#abstract class (we can create object)
from abc import abstractmethod
class theju:
    @abstractmethod
    def m1(self):
        pass
t=theju()
print(t)
print('================================')
#abstract class and abstract method(we can't create object)
from abc import ABC,abstractmethod
class theju(ABC):
    @abstractmethod
    def m1(self):
        pass
t=theju()
print(t)
print('================================')
