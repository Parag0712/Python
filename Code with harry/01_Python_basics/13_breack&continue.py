#break and continue 

for i in range(1,15):
    if(i == 13):
        break;
    if(i == 12):
        continue
    print("5 X",i,"=" ,i*5) 


# how we implement do while

i=0
while True:
    print(i)
    i+=1;
    if(i==20):
        break