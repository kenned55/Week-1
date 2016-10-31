import math 

num = int(input('Enter a number')) #1

num = math.factorial(num) #1

def Factorial(num):
    x = 0   #1
    
    while num % 5 == 0: #n
        x  += 1 #n
        num  = num / 5 #n
    else:   #n
        print (x) #n
 
      

Factorial(num) 
