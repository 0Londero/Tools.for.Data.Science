import matplotlib.pyplot as plt
import numpy as np

# Exercise 06: Subplots
#Line Plot
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.subplot(2,3,1)
plt.plot(x, y)
plt.title('Line Plot')
#Bar Plot
categories = ['A', 'B', 'C', 'D', 'E']
values = [5, 7, 3, 8, 6]
plt.subplot(2,3,2)
plt.bar(categories, values)
plt.title('Bar Plot')
#Histogram
data = np.random.randn(1000) #(1000 random values)
plt.subplot(2,3,3)
plt.hist(data)
plt.title('Histogram')
#Scatter Plot
x_scatter = np.random.rand(50)
y_scatter = np.random.rand(50)
plt.subplot(2,3,4)
plt.scatter(x_scatter, y_scatter)
plt.title('Scatter Plot')
plt.show()
