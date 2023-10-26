#Example for multi level inheritance
class grandpa:
    def G1(self):
        print('object class is a parent of grandfather(by default if dnt have any parent means, object class itself parent)')
class Father(grandpa):
    def F1(self):
        print('Grand father is a parent of father')
s=Father()
s.F1()
s.G1()
print(s.__str__())

