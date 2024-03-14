# 1+2+3+4+5

def factorial(n):
    fact =1;
    if( n==1 or n==0):
        return 1;
    else:
        return n*factorial(n-1);

# result = factorial(5)
# print(result)
def fibonacci(n):
    fact =1;
    if(n<=1):
        return n;
    else:
        return fibonacci(n-1)+fibonacci(n-2);

list = []
n = 10
for i in range(n):
    print(fibonacci(i))
