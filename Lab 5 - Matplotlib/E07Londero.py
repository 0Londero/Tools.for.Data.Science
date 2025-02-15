import matplotlib.pyplot as plt
import numpy as np

# Exercise 07
categories = ['Marketing', 'Development', 'Sales', 'Support']
values = [20, 35, 25, 20]

plt.pie(values, labels=categories)
plt.title('Pie chart')
plt.legend()
plt.show()