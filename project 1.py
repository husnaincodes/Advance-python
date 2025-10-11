import random
"""
-1 for snake 
0 for water 
1 for gun
"""
computer = random.choice([-1 ,0,1])

userchoice = input("Enter  your  choice (snake,water,gun) :")

userdic = {"snake":-1,"water":0,"gun":1}

reverseDic= {-1 :"snake", 0 : "water", 1:"gun"}

user = userdic[userchoice]

print(f"You choose  {reverseDic[user]}\nComputer choice  {reverseDic[computer]}")

if (computer==user):
    print("The match is draw !")
else:
    if (computer==-1 and user ==1):

        print("You win the game !")

    elif(computer==1 and user == -1):

        print("You lose computer win the game !")

    elif(computer==0 and user==-1):

        print("You win the game !")

    elif(computer==-1 and user== 0):

        print("You lose this game ! ")

    elif(computer==0 and user==1):

        print("You lose !")

    elif(computer==1 and user==0):

        print("You win the game !")
    else:
        print("Something went wrong !!!!")

