# Iterable and Enumerable:
    # List,Tuple,sting
# Iterable but not Enumerable:
    # set,dict
# Not Iterable:
    # enum



fruits = ['apple','banana','mango']
index=0

# 
for i in fruits:
    print(i)
    if(index ==1):
        print(i)
    index+=1
    
# easy way for this
for index,fruit in enumerate(fruits,start=1):
    if(1==index):
        print(f'{index} => {fruit} ')
    print(f'{index} => {fruit}')