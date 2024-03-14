# what is Dictionaries
# is a object

# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
# Dictionaries cannot have two items with the same key:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)


dic ={
    "firstName":"parag",
    "secondName":"vadgama"
}

print(dic["firstName"])
print(dic.get("firstName")) #give none if not found

for i in dic:
    print(dic[i])

print(dic.keys())

for i in dic.keys():
    print(f"key: {i} value: {dic[i]}")

for i in dic.values():
    print(i) 



# give key value pair
print(dic.items())

for key,value in dic.items():
    print(key,value)
