# sum number
def sumNumber(no):    
    rem = 0
    sum = 0
    while no>0:    
        rem = no%10;
        sum = sum+rem
        no = no//10
    
    return sum
no = int(input("Enter a number: "))
result = sumNumber(no)
print(result)