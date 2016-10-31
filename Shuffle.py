import random

x = [5,3,8,8,1,9,2,7] #1

for i in range(20):         #n           
    x += [x.pop(random.randint(0,7))] #n 

print (x) #1
