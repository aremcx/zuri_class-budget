class Dog:
    species = "Canis familiaris"
    print(species)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
       print (f"{self.name} is {self.age} years old")

    # Another instance method
    def speak(self, sound):
        print (f"{self.name} says {sound}")

miles = Dog("Miles", 9)
miles.species
miles.description()
miles.speak('Aaah')