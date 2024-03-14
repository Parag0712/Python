list = [1,2,41,3,4,12,1]
print(list.count(1))

# list.reverse() #change original list  reverse list 
# list.append(8) #append() method append value in last
# list.sort(reverse=True) #sort a list

# In Shallow copy, a copy of the original object is stored and only the reference address is finally copied.
# Here this one shallow copy if you copy like below bottom

list2 = list;   #shallow copy
list2[0] =12

# if change made in list2  then also change in list1
# so we have function which name copy() which make deep copy
# what is deep copy
# In Deep copy, the copy of the original object and the repetitive copies both are stored.

newList = list.copy() #deep copy 
newList[0] =14
print(list)
print(list2)
print(newList)

# Insert Method add value in specific index
newList.insert(1,"parag")
print(newList)

# extend() like (js spread operator)
cars = ['Ford', 'BMW', 'Volvo']
fruits = ['apple', 'banana', 'cherry']
newList1 = [1,2,3,5,7,"parag"]
# newList1.extend(cars,fruits)
# print(newList1)


# for multiple list extend

what = [newList1.extend(l) for l in (cars,fruits)] 

print(newList1)
print(what ,end="\n\n")

for l in (cars,fruits):
    print(l)

newM = cars+fruits # you can also concat list and make new list
newM[0] = "Range Rover"
print(newM)
print(cars)
print(fruits)
