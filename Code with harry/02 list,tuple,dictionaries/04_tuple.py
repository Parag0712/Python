#different between tuple and list is only [list] and (tuple)
#tuple are mutable not changeable
# tuple are constant list
# all thing smiler only different between tuple and list is (),[] and second is list are immutable(change) and tuple mutable(not change) 
tup = (1,2,3,"Parag",True)

print(type(tup),tup)
print(tup[-2]) #len(tup)-2
print(len(tup))

if 1 in tup:
    print("1 is present")
if 121 in tup:
    print("1 is present")

tup2 = tup[1:4]
print(tup2)

for i in range(0,len(tup),2):
    print(tup[i], end=" ")