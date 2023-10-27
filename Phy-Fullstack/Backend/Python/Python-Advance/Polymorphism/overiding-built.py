class cart:
    def __init__(self,b1,b2,b3):
        self.b1=b1
        self.b2=b2
        self.b3=b3
    def __len__(self):
        return(len(self.b1)+len(self.b2)+len(self.b3))

c=cart(['tops','saree','gown'],['phone','gold','laptop'],['roll','pizza']) 
print(c)
print(len(c))       