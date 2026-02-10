def greet():
    print("hello!!")
    print("Python learner!!")
    pass

greet()

def check_weather():
    temparature = 16;

    if temparature > 25:
        print("hot")
    else:
        print("its nice")

check_weather()

# Default values, params without default values need to be declared first
def greet(name, greeting = "Hello"):
    print(f"{greeting} , {name}")

greet("Sam") # Use default
# Recommendated to use keyword arguments
greet(name = "Sam", greeting= "Hi") # Hi, Sam
greet("Charlie", "Welcome") # Welcome, Charlie

def add_print(a, b):
    print(a + b)

add_print(a=5, b=10)

# return
def add_return(a, b):
    return a + b
# store the return
result = add_return(a=5, b=10)

def get_min_max_sum(numbers):
    return min(numbers), max(numbers), sum(numbers)

# Get all values
minimum, maximum, total = get_min_max_sum([5, 2, 8, 1, 9])
print(f"Min: {minimum}, Max: {maximum}, Sum: {total}")  # Min: 1, Max: 9, Sum: 25

# Or as a tuple
result = get_min_max_sum([5, 2, 8, 1, 9])
print(result)  # (1, 9, 25)