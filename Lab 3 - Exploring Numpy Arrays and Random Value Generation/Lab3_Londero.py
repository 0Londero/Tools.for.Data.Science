import numpy as np
import numpy.random
print(r"""
.____          ___.     _______  ________  
|    |   _____ \_ |__   \   _  \ \_____  \ 
|    |   \__  \ | __ \  /  /_\  \  _(__  < 
|    |___ / __ \| \_\ \ \  \_/   \/       \
|_______ (____  /___  /  \_____  /______  /
        \/    \/    \/         \/       \/ 
""")

# Task 01
# task01_array = np.array([1,2,3,4,5,6,7,8,...]
task01_array = np.arange(1,31,1)    # Using for create range
print(task01_array)
print()     # Space
print(task01_array[10])
print()     # Space

# Task 02
task02_array = np.reshape(task01_array,(6,5))
print(task02_array)
print()
print(task02_array[2,3])    # Answer 14
print(task02_array[3,4])    # Answer 20
print()

# Task 03
task03_array = task02_array
print(task03_array[2])
print(task03_array[:2,-3:])
print()

# Task 04
task04_array = numpy.random.randint(10,100,15)
print(f"The array is {task04_array}")
print()
print(f"the max value is {numpy.max(task04_array)} and the min is {numpy.min(task04_array)}")
print()

# Task 05
task05_array = numpy.random.randint (0, 50,16).reshape (4,4)
print(task05_array)
print(f" The sum is: {np.sum(task05_array)}")
print()

# Task 06
task06_array = numpy.random.randint (1,20,25).reshape (5,5)
print(task06_array)
print()
task06_array [1] = 0
print(task06_array)
print()
task06_array [task06_array > 10] = 99
print(task06_array)
print()

# Task 07
task07_array = numpy.random.randint (1,10,5)
task071_array = numpy.random.randint (1,10,5)

mult_07 = task07_array * task071_array
add_07 = task07_array + task071_array
subt_07 = task07_array - task071_array

print(f"Arrays {task07_array}\n       {task071_array}\n")
print(f" -- Multiplication: {mult_07}\n-- Addition: {add_07}\n-- Subtraction: {subt_07}")

# Task 08 # Broadcasting = Adding
print()
task08_array = numpy.array ([2,4,6,8])
task081_array = numpy.random.randint (1,5,12).reshape (3,4)
task08_result = task081_array + task08_array
print(task08_result)
print()

# Task 09
task09_array = numpy.random.randint (1,100,20)
print(task09_array [task09_array > 50])
task09_array [task09_array < 30] = -1
print(task09_array)
print()

# Task 10
task10_array = numpy.random.randint (1,50,12).reshape(3,4)
print(task10_array)
print()
task10_transposed = task10_array.T # Transpose, swap its rows and column
print(task10_transposed)
print()