def squareStar():
    '''
    doc string
        *****
        *****
        *****
        *****
        *****
    '''
    for i in range(0, 5):
        for j in range(0, 5):
            print("*", end="")
        print("")

def starRightAngled():
    '''
    doc string
        *
        **
        ***
        ****
    '''
    for i in range(0, 5):
        for j in range(0, i +1):
            print("*", end="")
        print("")

def starLeftAngled():
    '''
    doc string
        *****
        ****
        ***
        **
        *
    '''
    for i in range(5, 0,-1):
        for j in range(0, i ):
            print("*", end="")
        print("")


# Function Calling
# 1) => Square Star Pattern
squareStar()

# 2) => right-angled triangle
# The `# starLeftAngled()` line is a commented out function call. It is not being executed when the
# code is run.
# starRightAngled()

# 3) => left-angled triangle
# starLeftAngled()
