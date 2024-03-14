

def ageChecker(age):
    if age<18:
        raise ValueError("Enter a age 18")
    else:
        print("correct Age")

try:
    age= int(input("Enter a age: "))
    ageChecker(age);
except ValueError:
    print("value error")