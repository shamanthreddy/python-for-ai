try:
    age = int(input("Enter your age: "))
    print(f"In 10 yrs you will be {age + 10}")
except ValueError:
    print("Please enter a number")

try:
    with open('data/sales.csv', 'r') as f:
        content = f.read()
except FileNotFoundError:
    content = ""
print(content)

user = {'name': "Alice", "age": 25}
# Check if key exists
if "email" in user:
    print(user["email"])

# Use get() with default
email = user.get("email", "example@example.com")

# Or hadle with error
try:
    print(user["email"])
except KeyError:
    print("Email not found")
