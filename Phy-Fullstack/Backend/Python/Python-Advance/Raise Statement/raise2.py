class Eligible(Exception):
    pass
class not_Eligible(Exception):
    pass
u_value=18
while True:
    try:
        u_input=int(input('Enter the value: '))
        if u_input>u_value:
            raise Eligible
        elif u_input<u_value:
            raise not_Eligible
        break
    except(Eligible):
        print('You are eligible')
    except(not_Eligible):
        print('You are not eligible')
print('Congrats...')

            
    

