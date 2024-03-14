marks = [3, 5, 6, "Harry", True, 6, 7 , 2, 32, 345, 23]
print(marks[0:-5])
print(marks[0:len(marks)-5])

print(marks[1:4:1]) #Here first slice [1:4] =>[5,6,"Harry"] third argument for how many skip after first value
#5  ,Harry  [0]=5,[1]=6,[2]="harry"  0+2 = 2

# List comprehensions are used for creating new lists from other iterables like lists, tuples, dictionaries, sets, and even in arrays and strings.
str = "parag"

# list =[i for i in range(10)]
list =[i for i in range(10) if(i%2)==0]
print(list)