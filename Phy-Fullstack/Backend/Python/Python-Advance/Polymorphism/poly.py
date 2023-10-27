class vehicle:
    def __init__(self, name, color, price):
        self.name=name
        self.color=color
        self.price=price
    def details(self):
        print('Name of the vehicle:',self.name)
        print('Color of vehicle:',self.color)
        print('Price of the vehicle:',self.price)
class truck(vehicle):
    def max_speed(self):
        print('maximum speed limit 100')
    def gear(self):
        print('Gear change is 4')
class car(vehicle):
    def max_speed(self):
        print('maximum speed limit 150')
    def gear(self):
        print('Gear change is 5') 
    
t=vehicle('truck','red','500000')
t.details()
c=vehicle('car','blue','700000')
c.details()
