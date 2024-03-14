#how create function in python
def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)

def isGreater(a,b):
    if(a>b): return a
    elif (b>a): return b

def isLess(a,b):
    pass #using pass keyword like interface if you define 
#The pass statement is used as a placeholder for future code. When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed.

calculateGmean(1,2)
result = isGreater(1,2)
print(result)
# Python does not supp  ort function overloading. 

def add(a,b=2):
    print(a+b)
add(1)

def mul(a=1,b=4):
    print(a+b)
add(a=2,b=2)


