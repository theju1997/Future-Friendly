#by using abstract class ,abstract method
from abc import ABC,abstractmethod
class wifi(ABC):
    @abstractmethod
    def network(self):
        pass

class jio(wifi):
    def network(self):
        print('5g wifi with x')
    def network1(self):
        print('5g wifi with xy')

class Airtel(wifi):
    def network(self):
        print('6g wifi with xyz')

air=Airtel()
air.network()

j=jio()
j.network()
j.network1()
