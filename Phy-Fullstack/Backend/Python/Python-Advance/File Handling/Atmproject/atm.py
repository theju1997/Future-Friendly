u_pin=int(input('Enter Your secrate pincode:'))
f_pin=open('pin.txt','r')
f_read=int(f_pin.read())
f_pin.close()

if u_pin==f_read:
    print('Your pincode is correct')
    f_bal=open('bal.txt','r')
    bal=int(f_bal.read())
    f_bal.close()
    print('Your account balance is :',bal)
    print('1-Withdraw,2-Deposit')
    n=int(input())
    if n==1:
        print('withdraw')
        amount=int(input('Enter the amount'))
        bal=bal-amount
    elif n==2:
        print('Deposit')
    x=open('bal.txt','w')
    x.write(str(bal))
    x.close()
else:
    print('Your pincode is incorrect')