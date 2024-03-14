# String are immutable in python we cannot change by any method
a = "Pa rag  "
b = " !!!Harry!! !!!!!!!!! Harry!! "
print(a.upper())
print(a.lower())
print(b.strip("!"))
print(b.split("!"))

blogHeading = "introduction tO jS"
print(blogHeading.capitalize())

str1 = "Welcome to the Console!!!"
print(len(str1))

print(str1.center(50))#give space in start 
print(len(str1.center(30)))#here string length is 25 and center(30) 30-25 = 5 so add 5 space in front   
print(b.count("Harry")) 

str1 = "Welcome to the Console !!!"
print(str1.endswith("!!")) 
print(str1.endswith("!!",7,8))
print(str1.find("to")) #give first occurrence index of word
print(str1.index("Welcome")) #same like find but give exception

# isalnum() :
# The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.


str2 = "WelcomeToTheConsole"
print(str1.isalnum()) #false because of space "  "
print(str2.isalnum()) #true

# isalpha() :
# The isalnum() method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.

print(str1.isalpha())
print(str1.isascii()) #check char asci or not

# isprintable() :
# The isprintable() method returns True if all the values within the given string are printable, if not, then return False.

print(str1.isprintable())

# isspace() :
# The isspace() method returns True only and only if the string contains white spaces, else returns False.
str_1 = "        "       #using Spacebar
print(str_1.isspace())
str_2 = "        "       #using Tab
print(str_2.isspace())

# istitle() :
# The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False.

str_4 = "World Health Organization" 
print(str_4.istitle())

# swapcase() :
# The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper cas
str7 ="Python is a Interpreted Language"
print(str7.swapcase())