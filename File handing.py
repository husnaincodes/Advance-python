with open("data.txt","r") as f:
     text= f.read()
     print(text)


with open("write.txt","w") as m:
     rewite = m.write(text)