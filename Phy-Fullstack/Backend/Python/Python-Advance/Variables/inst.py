class Pen:
    def __init__(self,ink_color,price):
        self.ink_color=ink_color
        self.price=price
    def display(self):
        print('ink color is ',self.ink_color)
        print('pen price is',self.price)
brand1=Pen('Blue',30)
brand1.display()
brand2=Pen('Black',50)
brand2.display()