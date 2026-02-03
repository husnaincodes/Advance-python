import matplotlib.pyplot as plt
import numpy as np
 
language = ["python","c","c++","java","react"]
demand = [80,70,75,78,64]
demand2 = [60,50,45,38,24]
col = ["y","g","r","b","black"]
width = 0.2
p = np.arange(len(language))
p1 = [j+width for j in p]

plt.title("Programming Languages",fontsize=20)
plt.barh(p,demand,width,color="black",label="Popularity",)
plt.barh(p1,demand2,width,color="r",label="Popularity",)
plt.xlabel("Language")
plt.ylabel("Demand")

plt.xticks(p+width/2,language)
plt.legend()
plt.show()