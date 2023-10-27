class bank:
    bankname='SBI'
    r=12.25
    @staticmethod
    def simple_int(p,n):
        SIcount=(p*n*bank.r)/100
        print(SIcount)
bank.simple_int(20000,3)

