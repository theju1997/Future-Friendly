class ValueTooSmallError(Exception):
    pass
class ValueTooLargeError(Exception):
    pass
g_num=10
while True:
    try:
        u_num=int(input('Enter the guessing number'))
        if u_num<g_num:
            raise ValueTooSmallError
        elif u_num>g_num:
            raise ValueTooLargeError
        break
    except(ValueTooSmallError):
        print('The value is too small.try again!')
    except(ValueTooLargeError):
        print('The value is too small.try again!')
print('Congrats , your guessing number is correct')        

