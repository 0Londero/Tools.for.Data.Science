import matplotlib.pyplot as plt
import numpy as np


# Exercise 02: Customizing Plots
x = [0, 1, 2, 3, 4, 5, 6]
y = [0, 1, 4, 9, 16, 25, 36]
plt.plot(x, y, marker="o", color='#d4a373', linestyle= '--' )
plt.grid(color = '#fefae0', linewidth = 1) # Grid Lines
plt.show()