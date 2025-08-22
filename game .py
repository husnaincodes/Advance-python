
import random

   
computer = random.choice([-1,0,1])

userchoice = input("Enter your choice : {rock , paper ,scissors} : ")

userdic = { "rock" : -1,"paper":0,"scissors":1}

reversedic = {-1 :"rock",0 :"paper",1 : "scissors"}

user = userdic[userchoice]

print(f"You CHOOSE : {reversedic[user]}\nComputer Choose: {reversedic[computer]}")

if (computer==user):
    print("MATCH DRAW!")
else:
    if(computer==-1 and user == 0):
        print("You Win the Game!")
    elif(computer==0 and user==-1):
        print("You LOSE!")
    elif(computer==0 and user==1):
        print("You Win the Game!")
    elif(computer==1 and user==0):
        print("You LOSE!")
    elif(computer==-1 and user==1):
        print("You LOSE!")
    elif(computer==1 and user==-1):
        print("You  Win the Game! ")
    else:
        print("SOMETHING WENT WRONG!")
    
