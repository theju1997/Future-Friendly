class Ravikanth:
    house_name = 'Theju nilaya'

    def tmane(self):
        print(self.house_name)

class Suryakanth:
    house_name1 = 'Adi nilaya'

    def amane(self):
        print(self.house_name1)

r1 = Ravikanth()
print(r1.house_name)
r1.tmane()

s1 = Suryakanth()
print(s1.house_name1)
s1.amane()

#Example 2
class Employee:
    bonus=2000
    def display(self):
        print("this emlpoyee class method")

class Manager(Employee):
    bonus=5000
    def show(self):
        print("this manager class method")

m=Manager()
print(m.bonus)


