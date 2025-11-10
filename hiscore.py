
import random

def game():

 print("You are playing the game... ")

 score = random.randint(1,100)

 with open("hiscore.txt") as file:

    hiscore = file.read()

    if(hiscore!=""):
        hiscore = int(hiscore)

    else:
        hiscore = 0
 print(f"Your score {score}")

 if(score>hiscore):

    with open ("hiscore.txt","w") as file :

        file.write(str(score))

 return score

game()



