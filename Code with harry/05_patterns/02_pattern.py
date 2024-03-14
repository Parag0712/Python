
def numRightAngled():
    '''
    doc string
        1
        12
        123
        1234
        12345
    '''
    for i in range(1, 6):
        for j in range(1, i +1):
            print(j, end="")
        print("")
        
        
# numRightAngled()
def alphaPattern():
    '''
    A
    AB
    ABC
    ABCD
    ABCDE
    '''
    list = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ];  
    for i in range(5,0,-1):
        for j in range(0,i+1):
            print(list[j],end="")
        print()
        
def oddAlphaPattern():
    list = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ];  
    index=0
    for i in range(4,-1,-1):
        
        for j in range(i*2+1):
            print(list[i],end="")  
        print()

oddAlphaPattern()