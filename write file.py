
string = """"Python is a high-level, general-purpose programming language created by Guido van Rossum in 1991.
It is one of the most popular languages today because it is:


✅ Versatile – used in web development, data science, artificial intelligence,finance, etc."""


file = open("my_file","w")
file.write(string)
file.close()