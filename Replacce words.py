word = "Physics "
with open("my_file2.txt") as file :
    content = file.read()
new_content = content.replace(word,"Scientific study of nature")
with open("my_file2.txt",'w') as file :
    content = file.write(new_content)