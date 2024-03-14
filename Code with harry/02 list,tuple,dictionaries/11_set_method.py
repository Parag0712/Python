# https://replit.com/@codewithharry/32-Day32-Set-Methods#main.py

s ={1,2,3,4,5,"parag"}
s.add("vadgama")

s2 = {5,31,1,23,4,2}
print(s.union(s2),"union" ,end="\n\n") #common are intersection
print(s,end="\n\n")
print(s,s2 ,end="\n\n") #here value are same because of union

# if you went change original value then use update function

s.update(s2)
print(s ,end="\n\n")

# The intersection() and intersection_update() methods prints only items that are similar to both the sets. The intersection() method returns a new set whereas intersection_update() method updates into the existing set from another set.

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3= cities.intersection(cities2)
cities.intersection_update(cities2)

print(cities3)
print(cities,"intersection_update")

# III. symmetric_difference and symmetric_difference_update():
# The symmetric_difference() and symmetric_difference_update() methods prints only items that are not similar to both the sets. The symmetric_difference() method returns a new set whereas symmetric_difference_update() method updates into the existing set from another set.

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
cities.symmetric_difference_update(cities2)
print(cities)
print(cities3)

# IV. difference() and difference_update():
# The difference() and difference_update() methods prints only items that are only present in the original set and not in both the sets. The difference() method returns a new set whereas difference_update() method updates into the existing set from another set

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
# cities3 = cities.difference(cities2)
cities.difference_update(cities2)
print(cities) 
print(cities3)