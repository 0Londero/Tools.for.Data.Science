import matplotlib.pyplot as plt
import numpy as np

categories = ['Group 1', 'Group 2', 'Group 3']
value1 = np.array([5, 7, 3])
value2 = np.array([6, 8, 4])
value3 = np.array([4, 3, 5])

plt.bar(categories, value1, color='b', label='Value 1')
plt.bar(categories, value2, bottom=value1, color='r', label='Value 2')
plt.bar(categories, value3, bottom=value1 + value2, color='y', label='Value 3')

plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Plot Stacked')
plt.legend()
plt.show()
