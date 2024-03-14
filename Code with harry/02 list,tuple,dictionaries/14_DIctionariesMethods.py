ep1 = {
    122:93,
    123:93, 
    567:69,
    670:69
}
ep2 = {
    222: 67, 566: 90
}
print(ep1)
ep1.update(ep2)
print(ep1)
ep3 = ep1.copy() #for deep copy
# ep3 = ep1 #same shallow copy 

# ep3[567] = "parag" #
# print(ep3)
# print(ep1)
ep1.pop(122) #remove 122 key value
print(ep1)
# ep1.popitem() #pop random item
# ep1.popitem() #pop random item

# ep1.clear() #clear dictionaries
# del ep1  #if you not give key then delete Dictionaries  
del ep1[567]  #if you not give key then delete Dictionaries  
print(ep1)
print(ep1)


