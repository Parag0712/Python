# according to time give g,m,e
import time
t = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
print(type(hour))
hour = int(input("Enter hour: "))
print(hour)

if (0 <= hour < 12):
    print("Good Morning Sir!")
elif 12 <= hour < 17:
    print("Good Afternoon Sir!")
elif 17 <= hour < 0:
    print("Good Night Sir!")
