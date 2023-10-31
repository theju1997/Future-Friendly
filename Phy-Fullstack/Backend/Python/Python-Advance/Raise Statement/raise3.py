class price(Exception):
    pass
class lowprice(Exception):
     pass
b_price=400
while True:
    try:
        u_number=(int(input('Enter the number')))
        if u_number<b_price:
            raise lowprice
        elif u_number>b_price:
             raise price
            
    except(price):
            print('please take the book which one you want')
    except(lowprice):
            print('Bring more amount')
    print('You can choose the book which one you want ')