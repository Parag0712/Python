for i in range(5):
    if(i ==3):
        # break
        continue
    print(i)
else:
    print("sorry no i {}".format("parag"))
    print(f"sorry no i {'parag'}")
    

for x in range(5):
    print ("iteration no {} in for loop".format(x+1))
else:
    print ("else block in loop")
print ("Out of loop")