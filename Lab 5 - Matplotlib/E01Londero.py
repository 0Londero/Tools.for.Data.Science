import matplotlib.pyplot as plt


"""
years = [2025, 2026, 2027, 2028, 2029, 2030]
salaries = [46_000, 60_000, 100_000, 200_000, 220_000, 300_000]

plt.plot(years, salaries, "r--")

plt.xlabel("Year")
plt.ylabel("Salary")
plt.title("My Future Salary")
plt.y_ticks([46_000, 60_000, 100_000, 200_000, 220_000, 300_000],
           ["$46K", "$60K", "$100K", "$200K", "$220K", "$300K"])
"""

# Exercise 01: Basic Line Plot
x = [0, 1, 2, 3, 4, 5, 6]
y = [0, 1, 4, 9, 16, 25, 36]
plt.xlabel("numbers < 6")
plt.ylabel("big numbers")
plt.title("Lil Numbers <3")
plt.plot(x, y, )
plt.show()