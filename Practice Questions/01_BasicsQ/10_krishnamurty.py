# factorial
def factorial(value):
    sum =1
    for i in range(1,value+1):
        sum = sum*i;
    return sum

# Krishnamurti 
def Krishnamurti(no):    
    rem = 0
    arm = 0
    while no>0:    
        rem = no%10;
        krno += factorial(rem)
        no = no//10
    
    return krno
no = int(input("Enter a number: "))
result = Krishnamurti(no)
if no==result:
    print(f"{no} is ArmStrong")
else:
    print(f"{result} is not Armstrong")
