# Identation 

temp = 30;

if temp >= 30:
    print("its hot")
elif temp > 35:
    print("its very hot")
else:
    print("its nice")

# Loops

for i in range(5):
    print(f"{i} hello")

# Count from 1 to 5
for i in range(1, 6):
    print(i)
# Output: 1, 2, 3, 4, 5

# Count by 2s
for i in range(0, 10, 2):
    print(i)
# Output: 0, 2, 4, 6, 8

colors = ["red", "blue", "yellow"]
for color in colors:
    print(color)

# DataStructures

# list
mixed = ["Alice", 25, True, 3.14]  # Different types OK!

name = mixed[0]
age = mixed[1]
last = mixed[-1] # reverse; last item

fruits = ["apple", "banana", "orange"]
# Change an item
fruits[0] = "mango"
print(fruits)  # ["mango", "banana", "orange"]
# Add items
fruits.append("grape")      # Add to end
fruits.insert(1, "kiwi")    # Insert at position
# Remove items
fruits.remove("banana")     # Remove by value
last = fruits.pop()        # Remove and return last
del fruits[0]      

# dictionary

person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

person["age"]
person["license"] = True # add
del person["license"]

# Dictionary of dictionaries
students = {
    "alice": {"age": 20, "grade": "A"},
    "bob": {"age": 21, "grade": "B"},
    "charlie": {"age": 19, "grade": "A"}
}
# Access nested data
print(students["alice"]["grade"])  # "A"

# Tuples are like lists, but they can’t be changed once created

# Sets
empty_set = set()

numbers = {1, 2, 3, 4, 5}

# From a list (removes duplicates)
scores = [85, 90, 85, 92, 90]
unique_scores = set(scores)  # {85, 90, 92}