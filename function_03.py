

def greater (number1 ,number2, number3):

    if(number1>number2):

        return f"THE LARGEST NUMBER IS :{number1}"
    elif(number2>number3):
     return f"THE LARGEST NUMBER IS :{number2}"

    elif(number3>number1):

        return f"THE LARGEST NUMBER IS :{number3}"
    
number1= int(input("Enter your number : "))
number2= int(input("Enter your number : "))
number3= int(input("Enter your number : "))

print(greater(number1,number2,number3))