#how to insufficientfund
class InsufficientFund(Exception):
    pass
bal_amount=20000
while True:
    try:
        user_amount=int(input('Enter the amount to withdraw'))
        if user_amount>=bal_amount:
            raise InsufficientFund
        break
    except(InsufficientFund):
        print('Your amount is below the balance amount')
    
print('Please collect your amount')
