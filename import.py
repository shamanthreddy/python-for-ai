# Pattern 1: Import the whole module
import math
print(math.sqrt(16))

# Pattern 2: Import specific items from a module
from math import sqrt, pi
print(sqrt(16))


# Import entire module
import random
# Use module functions
number = random.randint(1, 10)
choice = random.choice([1,2,3])

# Date and time
import datetime
today = datetime.date.today()
print(today)

import json
data = {"name": "Sam", "age": 30}
json_string = json.dumps(data)
print(json_string)

import pandas as pd
df = pd.DataFrame(data)

# Web requests
import requests
response = requests.get('https://api.example.com/data')
data = response.json()

# Data analytics
import pandas as pd
# Create a simple DataFrame
data = {
    'name' : ['A', 'B', 'C'],
    'age' : [25, 30, 35],
    'state' : ['NV', 'LA', 'CA']
}

df = pd.DataFrame(data)
print(df)