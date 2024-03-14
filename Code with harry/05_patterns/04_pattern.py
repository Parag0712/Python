def Triangle(n: int):
    for i in range(n):
        # For printing the spaces before stars in each row
        for j in range(0,n - i - 1):
            print("", end="")

        # For printing the stars in each row
        for j in range(2 * i + 1):
            print("*", end="")

        # For printing the spaces after the stars in each row

        print()  # Move to the next line after each row

def triangle(n):
    for i in range(0,n):
        for j in range(0,n-i):
            print(" ",end="")
        for k in range(0,i+1):
            print("*",end=" ")
        print()

def revTriangle(n):
    for i in range(n,0,-1):
        for j in range(0,n-i):
            print(" ",end="")
        for k in range(0,i):
            print("*",end=" ")
        print()

revTriangle(6)
