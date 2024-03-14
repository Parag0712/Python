# what is sets 
# set if collection of well defined object
# not allow duplicate value
# Sets are unordered, so you cannot be sure in which order the items will appear.
# Sets are used to store multiple items in a single variable.
# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
# Sets cannot have two items with the same value.
# A set is a collection which is unordered, unchangeable*, and unindexed.

# The values True and 1 are considered the same value in sets, and are treated as duplicates:
# The values False and 0 are considered the same value in sets, and are treated as duplicates:  

s = {1,2,3,4,5,True,False} #1 is duplicate so remove automatically

print(s)
for i in s:
    print(i)

# s = {}
set = set() # we can make empty se like this

print(type(s))  #empty se give dictionary 