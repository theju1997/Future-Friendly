institute_name='apponix'
def f1_theju():
    print(institute_name)
    print("I like Blue")
def f1_Adi():
    print(institute_name)
    print("I like Red")
def f1_Shivu():
    print(institute_name)
    print("I like Black")
def f1_final():
    print(institute_name)
    print("I like magic color")    
    f1_theju()
    f1_Adi()
    f1_Shivu()
    f1_final()    

    #If we want to access global variable in local
    b=10
    def theju():
        global b
        print(b)
        a=40
        print(a)
        theju()
