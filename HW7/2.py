class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")
    
    def __str__(self):
        return f"Animal: {self.name}"
    def __repr__(self):
        return f"Animal(name={self.name})"

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def speak(self):
        print(f"{self.name} barks.")

    def __str__(self):
        return f"Dog: {self.name}"
    def __repr__(self):
        return f"Dog(name={self.name})"

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def speak(self):
        print(f"{self.name} meows.")

    def __str__(self):
        return f"Cat: {self.name}"
    def __repr__(self):
        return f"Cat(name={self.name})"
    
    
dog = Dog()
dog.speak()
cat = Cat()
cat.speak()
