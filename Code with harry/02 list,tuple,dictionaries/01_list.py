#list store multiple item in variable
#list store order collection
#list item separated by commas(,)
#list are mutable (changeable)
#List can store different type of data same variable
#List have index 0,1,2,3,4,5....

#tuple are not changeable

l = ["parag",1,2,3]
l[0] = "Vadgama"
print(l[0])
print(l[1])
print(l[2])
print(l[3])
print(len(l))
print(l[-3])
#how evaluate python (len(l)-3) 
#where negative index then same formula

for i in l:
    print(i,"list");
    

print(l.index(1)) 
# Return the number of times the value "cherry" appears in the fruits list:
print(l.count("parag"))
# if vadgama in list then print 
if "Vadgama" in l:
    print("parag")
elif 1 in l:
    print("1")
else:
    print("nothing")