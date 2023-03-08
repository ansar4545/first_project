import random as r

num = r.randrange(1,11)

i = 1
while(i <= 3):
    ask_user = int(input("Enter a num that you guess !! : "))

    if (ask_user == num):
        print("you guessed right , the number is {}".format(num))
        break 
    
    elif(ask_user < 0 or ask_user > 10):
        print("Enter valid numbers !!")

    i = i + 1
    

print("Randomly generated number is ", num )
    