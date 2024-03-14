# swap function
def swap(number_1,number_2):
    number_1 = number_2 +number_1
    number_2 = number_1 -number_2
    number_1 = number_1-number_2
    return number_1,number_2

# direct trick
def swapFunny(number_1,number_2):
    return number_2,number_1

value1 = int(input("Enter value-1 :"))
value2 = int(input("Enter value-2 :")) 
print(f"before swap value-1: {value1} and value-2: {value2}")
value1,value2 =  swapFunny(value1,value2)

print(f"after swap value-1: {value1} and value-2: {value2}")