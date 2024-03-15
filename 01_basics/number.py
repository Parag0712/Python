import math
import random
# number is group of object decimal fraction 

a = 10;
b = 20;
c = 30;
print(a/b)
print(a//b)
print(int(40+2.23));
print(float(40+2.23));
print('chai'+'code');
print(a,b,c);
print(a+1,b*2,c+1);
print(a+1,b**2,c+1);
# print(2**1000000); 
# Python handle bigger number easily 
# 1.0715086071862673e+301 in js E come 
print(1/7.0);
print(repr('paragasda////'));
print(str('paragasda'));
print(1==1.0); #true
print(1!=0.5);

# Chained comp

print(a<b<c);
print(a<b and b<c);
print(1==2<3);
print(1==2 and 1<3);

print(math.floor(2.6));
print(math.ceil(2.6));
print(math.trunc(20.0));

print(200**2);
print((2+2j)*3);

# Octal  => base to the 8 
print(0o20)
print(0xFF)

# Binary 
print(0b100)
print(oct(65))
print(hex(65))
print(bin(65))
print(bin(65))
print(int('64',8))
print(int('64',16))

# Bit wise operator

num1 = 12;  
num2 = 15;
print(num1<<2);
print(num1>>2);

print(random.random())
print(random.randint(1,200))

l1 = ['lemon','masala','black','mint'];
print(random.choice(l1))
# Output: List of 3 random elements from l1, with possible duplicates
print(random.choices(l1,k=10))

shuffleList = l1.copy();
random.shuffle(shuffleList)
print(shuffleList)
print(l1)

# For Decimal 
from decimal import Decimal
ans = Decimal('0.1') + Decimal('0.1')+Decimal('0.1')- Decimal('0.3');
print(ans)
print((0.1+0.1+0.1)-0.3)
from fractions import Fraction
# For Fraction
myFra = Fraction(2,7) * Fraction(1,2)

print((2/7)*(1/2));
print(myFra)


# Sets 
# Now You can perform Set maths here
setOne = {1,2,3,4}
setTwo = {1,3,7,2}
print(type(setOne))
print(setOne & setTwo)
print(setOne | setTwo)
print(setOne - setTwo)


print(True == 1);
print(False == 0);

print(1 is 1);
print(True is 1);

print(True +5);