import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
z = [11,22,33,44,55]

plt.plot(x, y,color="r",label=" Line Graph")
plt.plot(x, z,color="b",label=" Line Graph")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("My First Plot")

plt.legend()
plt.show()
