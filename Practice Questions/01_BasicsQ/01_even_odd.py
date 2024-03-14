# function for odd even number
def oddEven(value):
    if value%2==0:
        return f"{value} is even"
    else:
        return f"{value} is odd"

value = int(input(f"Enter a number check: "))
for i in range(value):
    print(oddEven(i))    

