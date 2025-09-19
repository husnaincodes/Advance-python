
def fahrenheit_to_celsius(fahrenheit):

    return 5*(fahrenheit-32)/9

fahrenheit_value = int(input("Enter the temperature :  "))

round = round(fahrenheit_to_celsius(fahrenheit_value),2)

print(f"{round}°C")
