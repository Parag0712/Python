no=int(input("Enter no =>"))
rem=0

def reverseNumber(no):
    reminder=0
    rev=0
    while(no>0):
        reminder = no%10
        rev = rev*10+reminder
        no=no//10
    return rev
print("Reverse no =",reverseNumber(no))

