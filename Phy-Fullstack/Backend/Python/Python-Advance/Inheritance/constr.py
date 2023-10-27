class Father:
    def __init__(self):
        print('father constructor called')
        self.vehicle='Bike'
        print(self.vehicle)
class son(Father):
    pass
s=son()
