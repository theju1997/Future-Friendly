#to understand try ,except, finaaly
try:
    try:
        print('i am try')
    except:
        print('i am except')
except:
    try:
        print('i am except try')
    except:
        print('i am  except try')
    finally:
        print('i am except finally')    
finally:
    try:
        print('i am finally')
    except:
        print('i am finally except')
    finally:
        print('i am final finally')