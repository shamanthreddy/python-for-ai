name = "Alice"
age = 25


""" this is a multi-line
comment
this can be used to describe functions
"""

# nunbers

total = 5 + 5

power = 10 ** 2

cubed = 2 ** 3

division = 10 / 3 

division = 10 // 3 # rounds down


# Strings

string = "My name is Shamanth"

my_long_string = """My name is 
Shamanth
"""

first_name = "Shamanth"
last_name = "Mittapalli"

full_name = first_name + " " + last_name

long_dash = "-" * 19
print(full_name)
print(long_dash)

len(long_dash)
len(full_name)

age = 25
message = "I am " + str(age) + " years of age"
print(message)

message = f"I am {age} years of age"
print(message)

# boolean

is_ready = True

age = 25

print(age == 25)
print(age != 30)
print(age > 20)
print(age < 30)

# Operators

result = 2 + 3 * 4 # 14
result = (2 + 3) * 4 # 20 

# logical

age = 25
has_license = False

can_drive = age >= 16 and has_license
print(can_drive) # True

has_license = False

can_drive = age >= 16 or has_license
print(can_drive) # True

x = 10;
x += 5 # 15
x *= 2 # 30

# String methods

text = "Python is nice"
print(text.upper())
print(text.lower())
print(text.title())

price = "$19.99"
print(price.strip("$"))  # "19.99"

message = "I love Python programming with Python"

# Check if something exists
print("Python" in message)        # True
print(message.startswith("I"))   # True
print(message.endswith("Python")) # True

# Find position
print(message.find("Python"))     # 7 (first occurrence)
print(message.count("Python"))    # 2 (number of times)

# Replace
new_message = message.replace("Python", "JavaScript")
print(new_message)  # "I love JavaScript programming with JavaScript"

