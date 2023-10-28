#By using two methods 
from abc import ABC,abstractmethod
class wifi(ABC):
    @abstractmethod #method
    def network(self):
        pass
    @abstractmethod #method
    def charges(self):
        pass
    def enjoy(self):#normal method
        print('enjoy is norma method we can implement without creating class')

class jio(wifi):
    def network(self):
        print('5g wifi with x')
       

class Airtel(jio):
    def charges(self):
        print(' 2 paise tariff')

air=Airtel()
air.network()
air.charges()
air.enjoy()