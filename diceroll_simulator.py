import random as r

print(" what do you want to do : 1. roll the dice 2. exit ")
num = int(input("Enter a num (1 or 2): "))

if (num == 1):
    print(r.randrange(1,7))

elif(num == 2):
    print("you exit from the simulation")
    
else:
    print("Enter valid numbers ")


    

