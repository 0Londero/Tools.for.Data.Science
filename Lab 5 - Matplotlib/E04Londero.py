import matplotlib.pyplot as plt
import numpy as np

# Exercise 04: Histogram
data = np.random.normal(0, 1, 500)
# 500 data points from a normal distribution
plt.hist(data, bins=20, edgecolor='#0077b6', color='#00b4d8')
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()