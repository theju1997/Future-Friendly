class BMW:
    def fuel_type(self):
        print("Diesel")
    
    def max_speed(self):
        print("Max speed is 200")

class Swift:
    def fuel_type(self):
        print('Petrol')
    
    def max_speed(self):
        print('Max speed is 150')

def car_details(theju):
    theju.fuel_type()
    theju.max_speed()

bmw = BMW()
car_details(bmw)

swift = Swift()
car_details(swift)
    