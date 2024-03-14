#The GCD of two or more integers is the largest positive integer that divides each of the integers without leaving a remainder.
# GCD (greatest common divisible) for example
# 18 & 12 6*3 6*4

# simple approach for solve this question 

def findGCD(no_1: int,no_2:int):
    temp = 0; 
    # compare value 
    if(no_1>no_2): temp = no_1
    else: temp = no_2
    for i in range(temp,1,-1):
        if(no_1%i==0 and no_2%i==0):
            return f"{i} is GCD"
            break;

print(findGCD(12,18))
