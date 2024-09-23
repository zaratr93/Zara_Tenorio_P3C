import math
def factorial(n):
    result = 1 
    for i in range(2,n+1):
        result *= i
    print(result)
    
factorial(6)
factorial(11)
factorial(15)
factorial(22)

def remainder(x,y):
   print(x-(y*(math.floor(x/y))))
   
remainder(3,2)
remainder(21,4)
remainder(131,19)
remainder(81,9)





