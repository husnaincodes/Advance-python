import os
with open("python.txt","r") as f:
    data = f.read()
    new_data = data.replace("java","Python")
    print(new_data)


with open("python.txt","w") as f:
    data = f.write(new_data)