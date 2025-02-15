import matplotlib.pyplot as plt
import numpy as np

dataset1 = np.random.normal(60, 10, 100) # 100 data points around mean 60
dataset2 = np.random.normal(70, 15, 100) # 100 data points around mean 70
dataset3 = np.random.normal(80, 5, 100) # 100 data points around mean 80

plt.boxplot([dataset1, dataset2, dataset3])
plt.title('Box plot')
plt.xlabel ('Dataset')
plt.ylabel('Range')
plt.show()