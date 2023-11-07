#to create thread
#using threading module
#one task multi thread
#Joining thread
import threading

def listen_song():#task 1
    print('lyrics of favorite song')

t1=threading.Thread(target=listen_song) #module 
t2=threading.Thread(target=listen_song)
t3=threading.Thread(target=listen_song)
t1.start()
t2.start()
t3.start()
#=======================================================
import threading

def listen_song():#task 1
    print('Songs')

def listen_song1():#task 2
    print('videos')

def listen_song2():#task 3
    print('Games')
t1=threading.Thread(target=listen_song) #module 
t2=threading.Thread(target=listen_song1)
t3=threading.Thread(target=listen_song2)
t1.start()
t2.start()
t3.start()
#===========================================================

def dance_type1():
    print('Western dance')

def dance_type2():
    print('Bolly wood dance')

d1=threading.Thread(target=dance_type1)
d2=threading.Thread(target=dance_type2)
d1.start()
print(d1)#to check thread name 
d2.start()
print(d2)
#==============================================================
##def task1():#task 1
##    print(threading.current_tgread)
##
##def task2():#task 2
##    print(threading.current_tgread)
##
##t1=threading.Thread(target=task1 ,name='theju') #name=theju is a thread name we are giving other wise it will give thread 1 etc
##t2=threading.Thread(target=task2)
##t1.start()
##t2.start()

#=============================================================
import threading
import time

def disp():
    print('Good morning Theju')
    time.sleep(10)
    print('After 10 second printing ---Good evening')
t1=threading.Thread(target=disp)
t1.start()
#==============================================================
import threading
import time

def disp():
    print('Good morning Theju')
    time.sleep(10)
    print('After 10 second printing ---Good evening')
for x in range(5):
    
    t1=threading.Thread(target=disp)
    t1.start()
#================================================================
import threading
import time

def disp1():
    for x in range(5):
        print('Thread1 running')
        time.sleep(2)
def disp2():
    for x in range(5):
        print('Thread2 running')
        time.sleep(4)
  
    
t1=threading.Thread(target=disp1)
t2=threading.Thread(target=disp2)
t1.start()
t2.start()
#================================================================
import threading
import time

def disp1():
    for x in range(5):
        print('Thread1 running')
        time.sleep(2)
def disp2():
    for x in range(5):
        print('Thread2 running')
        time.sleep(4)
  
    
t1=threading.Thread(target=disp1)
t2=threading.Thread(target=disp2)
t1.start()
t1.join()  #If we give join method after the thread 1 only thread 2 is foining to print
t2.start()
#=================================================================
import threading
import time

def disp1():
    for x in range(5):
        print('Thread1 running')
        time.sleep(2)
def disp2():
    for x in range(5):
        print('Thread2 running')
        time.sleep(4)
  
    
t1=threading.Thread(target=disp1,name='water')
print(t1)####
t2=threading.Thread(target=disp2,name='oil')
print(t2) ###
t1.start()
t1.join()  #If we give join method after the thread 1 only thread 2 is foining to print
t2.start()
#====================================================================
















