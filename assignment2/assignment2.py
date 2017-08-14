import math
def checker (number):
    z = int(math.sqrt(number))
    test = True;
    for i in range(2,z+1):
        if (number%i==0):
            test = False
    return test
sumgLogs = 0
for x in range(1,10):
    
    if (x%2 != 0):
        if (checker(x) == True):
            sumgLogs += math.log(x,2)
            print x
             

print sumgLogs

print math.log(7)
        
        
    