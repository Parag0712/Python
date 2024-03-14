# replacement of switch case
x = int(input("Enter the value of x:"))
match x:
    case 0:
        print("x is a zero")
    case 3:
        print("case is 3")
    case _ if x != 90:
        print("90 for default")
    case _ if x!=80:
        print(x, "is not 80")
    case _:
        print("_ for default")

