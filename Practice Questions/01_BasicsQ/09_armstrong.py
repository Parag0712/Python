def armStrongNum(no):    
    rem = 0
    arm = 0
    while no>0:    
        rem = no%10;
        arm = arm +(rem*rem*rem)
        no = no//10
    
    return arm
no = int(input("Enter a number: "))

result = armStrongNum(no)
if no==result:
    print(f"{no} is ArmStrong")
else:
    print(f"{result} is not Armstrong")
