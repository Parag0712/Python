name = "Harry"
friend = "Rohan"
anotherFriend = 'Lovish'
# string in syntax
apple = '''He said, 
Hi Harry
hey I am good
"I want to eat an apple'''

# string in syntax
apple = '''
Hi Harry
hey I am good
"I want to eat an apple'''


print("Hello, " + name)
# print(apple) 
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
# print(name[5]) # Throws an error
print("Lets use a for loop\n")
for char in name:
    print(char, end='')