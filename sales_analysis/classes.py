class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color

jerry = Dog(name="Jerry", breed="lab")
print(jerry.name + " " + jerry.breed)

class APIConfig:
    def __init__(self, api_key, model="gpt-3.5-turbo", max_tokens = 100):
        self.api_key = api_key
        self.model = model
        self.max_tokens = max_tokens 
        self.base_url = "https://api.openai.com/v1"

# Create different configurations
dev_config = APIConfig("sk-dev-key", max_tokens=50)

prod_config = APIConfig(api_key="sk-prod-key", model="gpt-4", max_tokens=1000)

print(dev_config.model)
print(prod_config.model)

class DataValidator:
    def __init__(self):
        self.errors = []

    def validate_email(self, email):
        if '@' not in email:
            self.errors.append(f"Invalid email: {email}")
            return False
        return True

    def validate_age(self, age):
        if age < 0 or age > 150:
            self.errors.append(f"Invalid age: {age}")
            return False
        return True
    
    def get_errors(self):
        return self.errors
    
validator = DataValidator()

validator.validate_email(email="bad_email")
validator.validate_age(age=200)

print(validator.get_errors())

validator.validate_email("sam@edtech.edu")
validator.validate_age(age=80)

# Real world use-case of Inheritance

class BaseModel:
    def __init__(self, model_name):
        self.model_name = model_name
        self.is_loaded = False
    
    def load(self):
        print(f"Loading {self.model_name}...")
        self.is_loaded = True

class TextModel(BaseModel):
    def __init__(self, model_name, max_length = 1000):
        super().__init__(model_name)
        self.max_length = max_length

    def process_text(self, text):
        if not self.is_loaded:
            self.load()

        #Truncate if needed
        if len(text) > self.max_length:
            text = text[:self.max_length]
        return f"Processed: {text}"
    
model = TextModel(model_name="gpt-3.5-turbo", max_length=100)

# Call method - notice no 'self' parameter needed
result = model.process_text(text="Hello world")
print(result)  # Loading gpt-3.5-turbo...
               # Processed: Hello world


# Overriding methods
class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def make_sound(self):  # Override parent method
        return f"{self.name} barks: Woof!"

class Cat(Animal):
    def make_sound(self):  # Override parent method
        return f"{self.name} meows: Meow!"

# Different animals, different sounds
generic = Animal(name="Something")
dog = Dog(name="Buddy")
cat = Cat(name="Whiskers")

print(generic.make_sound())  # Something makes a sound
print(dog.make_sound())      # Buddy barks: Woof!
print(cat.make_sound())      # Whiskers meows: Meow!