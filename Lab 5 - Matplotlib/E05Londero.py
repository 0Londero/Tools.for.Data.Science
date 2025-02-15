import matplotlib.pyplot as plt
import numpy as np

# Exercise 05: Scatter Plot
x = np.random.rand(50) # 50 random x-values between 0 and 1
y = np.random.rand(50) # 50 random y-values between 0 and 1
plt.scatter(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Scatter Plot")
plt.show()