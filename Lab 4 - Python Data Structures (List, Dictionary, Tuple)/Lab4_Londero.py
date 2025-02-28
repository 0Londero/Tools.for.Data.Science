# DICTIONARIES E TUPLES E LIST EXERCISES

import numpy as np


print(r"""
.____          ___.     _______      _____  
|    |   _____ \_ |__   \   _  \    /  |  | 
|    |   \__  \ | __ \  /  /_\  \  /   |  |_
|    |___ / __ \| \_\ \ \  \_/   \/    ^   /
|_______ (____  /___  /  \_____  /\____   | 
        \/    \/    \/         \/      |__| 
""")

"""
0. add new key-value pair
capital_cities["South Korea"] = "Seoul"

1. delete key-value pair
del capital_cities["Italy"]

2. update value
capital_cities["Italy"] = "Rome"
print(capital_cities)

[(k1, v1), (k2, v2), ...]
for (k, v) in capital_cities.items():
    print(f"key: {k}, value: {v}")

for v in capital_cities.values():
    print(f"value: {v}")

for k in capital_cities.keys():
    print(f"value: {k}")
"""

# Exercise 01
students = {
"Alice": [85, 78, 92],
"Bob": [79, 74, 81],
"Charlie": [91, 82, 85],
"David": [76, 85, 83],
"Eve": [88, 79, 92]
}
average_score = {}

for key,value in students.items():
    print(f"Student: {key}| Average Score: {np.average(value):.2f}") # 1
    average_score[key] = np.average(value)

# The get() method returns the value of the item with the specified key.
highest_score = max(average_score, key=average_score.get) # Here it's telling that the key is the result of average score
lowest_score = min(average_score, key=average_score.get) # print(average_score.get("Bob"))
# key is used to specify a value for the function to look at

print(f"Highest Score: {highest_score}| {average_score[highest_score]}") # 2
print(f"Lowest Score: {lowest_score}| {average_score[lowest_score]}") # 3
print()

students["Frank"] = [80, 90, 85]
print(students) # 4
print()
print()

# Exercise 02
inventory = {
 "apple": (50, 0.5),
 "banana": (100, 0.2),
 "orange": (75, 0.3),
 "pear": (20, 0.4)
}
total_product_value  = {}
for key, value in inventory.items():
    print(f"Current Product: {key}  | Quantity: {value[0]}  | Price: {value[1]}") # 1
    total_product_value [key] = value[0] * value[1]

total_inventory_value = np.sum([total_product_value[key] for key in total_product_value.keys()])
print(f"The total inventory VALUE is:   ${total_inventory_value}")# 2

inventory["mango"] = (30, 0.6) # 3
inventory["banana"] = (120, 0.2)
print()
print(inventory) # 4
del inventory["pear"]
print(inventory) # 5

# Exercise 03
print()
print()
employees = [
 ("John Doe", "Accounting", "john.doe@example.com"),
 ("Jane Smith", "Marketing", "jane.smith@example.com"),
 ("Emily Davis", "HR", "emily.davis@example.com"),
 ("Michael Brown", "IT", "michael.brown@example.com")
]
for item in employees:
    print(f"Employee Name: {item[0]} | Department: {item[1]}| E-mail: {item[2]}",) #1
print()
print()

def last_name (employee):
    full_name = employee[0]
    last_n = full_name.split()[-1]
    return last_n


employees.sort(key=last_name) #2
for item in employees:
    print(f"Employee Name: {item[0]} | Department: {item[1]}| E-mail: {item[2]}",) #2
print()

employees.append(["David Wilson", "Sales", "david.wilson@example.com" ])
for item in employees:
    print(f"Employee Name: {item[0]} | Department: {item[1]}| E-mail: {item[2]}",) #3

for item in employees:
    if item[0] == "Jane Smith":
        print(f"\n Jane Smith works in the {item[1]} department") #4

# Exercise 04
print()
library = {
"978-3-16-148410-0": {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951},
"978-0-14-028329-7": {"title": "1984", "author": "George Orwell", "year": 1949},
"978-0-7432-7356-5": {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
"978-0-452-28423-4": {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932}
}

for key, value in library.items(): #1
    print (f"The current book ISBN is = {key}")
    print (f"Title: {value['title']} | Author: {value['author']} | Year: {value['year']}")

print()
print(library["978-0-14-028329-7"]) # 2
library ["978-1-4028-9462-6"] = {"title": "The Great Gatsby", "author": "F.Scott Fitzgerald", "year": 1925}# 3
library["978-0-7432-7356-5"]["year"] = 1961 # 4
del library["978-0-452-28423-4"] # 5
print()
print()
for key, value in library.items():
    print (f"The current book ISBN is = {key}")
    print (f"Title: {value['title']} | Author: {value['author']} | Year: {value['year']}")# 5

# Exercise 05
cities = {
 "New York": 8419000,
 "Los Angeles": 3980000,
 "Chicago": 2716000,
 "Houston": 2328000,
 "Phoenix": 1690000
}
print()
for k,v in cities.items():
    print(f"City: {k} | Population: {v}") #1
print()
highest_population = max(cities, key=cities.get)
lowest_population = min(cities, key=cities.get)

print(f"Highest Population: {highest_population}, Population of {cities[highest_population]}")# 2
print(f"Lowest Population: {lowest_population}, Population of {cities[lowest_population]}")# 3
print()

cities ["Phoenix"] = 1700000
for k,v in cities.items():
    print(f"City: {k} | Population: {v}")# 4

cities ["San Francisco"] = 884000
print()
for k,v in cities.items():
    print(f"City: {k} | Population: {v}")
print()

# Exercise 06
movies = {
"Inception": {"year": 2010, "rating": 8.8, "genre": "SciFi"},
"The Godfather": {"year": 1972, "rating": 9.2, "genre": "Crime"},
"The Dark Knight": {"year": 2008, "rating": 9.0, "genre": "Action"},
"Pulp Fiction": {"year": 1994, "rating": 8.9, "genre": "Crime"},
"Forrest Gump": {"year": 1994, "rating": 8.8, "genre": "Drama"}
}

for k,v in movies.items():
    print(f"_______________{k}_______________")
    print(f"Year: {v['year']} || Rating: {v['rating']} || Genre: {v['genre']}") #1

def get_rating (movie_name):
    return movies[movie_name]["rating"]
print()
highest_rated_movie = max(movies, key=get_rating)
print(f"Highest Rated Movie: {highest_rated_movie}") #2
print()

movies["The Matrix"] = {"year": 1999, "rating": 87, "genre": "Sci-Fi"} #3
movies["Inception"]["rating"] = 9.0

for k,v in movies.items():
    print(f"_______________{k}_______________")
    print(f"Year: {v['year']} || Rating: {v['rating']} || Genre: {v['genre']}") #4

print()

del movies["Pulp Fiction"]

for k,v in movies.items():
    print(f"_______________{k}_______________")
    print(f"Year: {v['year']} || Rating: {v['rating']} || Genre: {v['genre']}") #5
print()

# Exercise 07
countries = {
 "USA": "Washington, D.C.",
 "Canada": "Ottawa",
 "France": "Paris",
 "Germany": "Berlin",
 "Japan": "Tokyo"
}

for k,v in countries.items():
    print(f"Country: {k}    ||      Capitals: {v}") #1

for k,v in countries.items():
    if k == "Germany":
        print(f"The capital is: {[v]}") #2

countries["Australia"] = "Canberra"
for k,v in countries.items():
    print(f"Country: {k}    ||      Capitals: {v}") #3
print()

countries["USA"] = "New Washington"
for k,v in countries.items():
    print(f"Country: {k}    ||      Capitals: {v}") #4
print()
del countries["France"]

for k,v in countries.items():
    print(f"Country: {k}    ||      Capitals: {v}") #5
print()

# Exercise 08
cart = [
 {"item": "apple", "quantity": 3, "price_per_unit": 0.5},
 {"item": "banana", "quantity": 6, "price_per_unit": 0.2},
 {"item": "orange", "quantity": 4, "price_per_unit": 0.3},
 {"item": "pear", "quantity": 2, "price_per_unit": 0.4}
]

for item in cart:
    print(f"Item:    {item['item']}| Quantity: {item['quantity']}| Price per unit: ${item['price_per_unit']}",) #1

total_cost = sum(item["quantity"] * item["price_per_unit"] for item in cart)
print(f"\nTotal Cost of the Cart: ${total_cost:.2f}") #2

cart.append({"item": "grape", "quantity": 5, "price_per_unit": 0.6}) #3

for item in cart:
    if item["item"] == "banana":
        item["quantity"] = 10
print()
for item in cart:
    print(f"Item:    {item['item']}| Quantity: {item['quantity']}| Price per unit: ${item['price_per_unit']}",) #4
print()
cart = [item for item in cart if item["item"] != "pear"]
for item in cart:
    print(f"Item:    {item['item']}| Quantity: {item['quantity']}| Price per unit: ${item['price_per_unit']}",) #5

# Exercise 9
weather = {
    "Monday": {"temperature": 20, "humidity": 60},
    "Tuesday": {"temperature": 22, "humidity": 55},
    "Wednesday": {"temperature": 19, "humidity": 65},
    "Thursday": {"temperature": 23, "humidity": 50},
    "Friday": {"temperature": 21, "humidity": 70}
}

for day, data in weather.items():
    print(f"{day}--> Temperature = {data['temperature']}°C  ||   Humidity = {data['humidity']}%")
print()

def get_temperature(d):
    return weather[d]["temperature"]
def get_humidity(d):
    return weather[d]["humidity"]

hottest_day = max(weather, key=get_temperature)
print(f"The hottest day is {hottest_day} with {weather[hottest_day]['temperature']}°C")# 2
lowest_humidity_day = min(weather, key=get_humidity)
print(f"The day with the lowest humidity is {lowest_humidity_day} with {weather[lowest_humidity_day]['humidity']}%")# 3
print()
weather["Wednesday"]["temperature"] = 25
for day, data in weather.items():
    print(f"{day}--> Temperature = {data['temperature']}°C  ||   Humidity = {data['humidity']}%")# 4
print()
print()
weather["Saturday"] = {"temperature": 24, "humidity": 60}
for day, data in weather.items():
    print(f"{day}--> Temperature = {data['temperature']}°C  ||   Humidity = {data['humidity']}%")# 5
print()

# Exercise 10
print()
members = [
    {"name": "Alice", "age": 25, "books_borrowed": ["1984", "To Kill a Mockingbird"]},
    {"name": "Bob", "age": 30, "books_borrowed": ["The Catcher in the Rye"]},
    {"name": "Charlie", "age": 22, "books_borrowed": ["Brave New World", "1984"]},
    {"name": "David", "age": 35, "books_borrowed": ["The Great Gatsby"]}
]

for member in members:
    print(f"{member['name']}    -->     Age: {member['age']}")# 1
print()
charlie_books = next(m["books_borrowed"] for m in members if m["name"] == "Charlie")
print("Books borrowed by Charlie:", charlie_books)# 2

members.append({"name": "Eve", "age": 28, "books_borrowed": ["Pride and Prejudice"]})# 3
for member in members:
    if member["name"] == "Bob":
        member["age"] = 31
print()
for member in members:
    print(f"{member['name']} || Age: {member['age']}  || Books Borrowed: {member['books_borrowed']}")# 4
print()
members = [m for m in members if m["name"] != "David"]
for member in members:
    print(f"{member['name']} || Age: {member['age']}  || Books Borrowed: {member['books_borrowed']}")# 5