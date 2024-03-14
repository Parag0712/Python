def nStarTriangle(n: int) :
    for i in range(0,n):
        for j in range(1,i+1):
            print("*",end="")
        print("")

        # reversed
    for i in range(n,0,-1):
        for k in range(1,i+1):
            print("*",end="")
        print("")

nStarTriangle(3)

def seeding(n: int) -> None:
    # Write your solution here.
        for i in range(n,0,-1):
            for j in range(0,i):
                print('*',end="")
            print("")

seeding(3)
