a = int(input("Enter your age: "))
print("Your age: ",a);
if(a>18):
    print("You can drive")
else:
    print("you cannot drive")

num = 10
if(num<0):
    print("Number is negative.")
elif(num>0):
    if(num<=10):
        print("Number is between 1-10")
    elif(num>10 and num<=10):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")