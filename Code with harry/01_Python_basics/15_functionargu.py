# for tuple
# (*) for iterable like tuple ,dict,list,set  now you give argument then take as tuple
def sumOfNumber(*number):     
    sum=0
    print(type(number))#type is tuple 
    for i in number:
        sum +=i
    return sum


a = sumOfNumber(1,2,4)
print(a)

# (**) for dict  (Object)
def introName(**names):
    print("hello my name:",names["name"],"my hobby: ",names["hobby"],"My inspiration: ",names["inspiration"])
    
    
introName(name="parag",hobby="be ....",inspiration="Mere father")