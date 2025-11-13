#!/usr/bin/python3

"""
Demonstrates class definitions and object-oriented programming in Python.
"""


class Animal:
    """A base Animal class"""

    # Class variable
    kingdom = "Animalia"

    def __init__(self, name, age):
        """Initialize a new Animal object

        Args:
            name (str): The animal's name
            age (int): The animal's age in years
        """
        self.name = name
        self.age = age

    def __str__(self):
        """Return a string representation of the Animal"""
        return f"{self.name} is {self.age} years old"

    def make_sound(self):
        """Make a generic animal sound"""
        return f"{self.name} makes a sound"

    def birthday(self):
        """Increment the animal's age by 1"""
        self.age += 1
        return f"{self.name} is now {self.age} years old!"


class Dog(Animal):
    """A Dog class that inherits from Animal"""

    # Class variable specific to dogs
    species = "Canis familiaris"

    def __init__(self, name, age, breed=None):
        """Initialize a new Dog object

        Args:
            name (str): The dog's name
            age (int): The dog's age in years
            breed (str, optional): The dog's breed
        """
        # Call the parent class's __init__ method
        super().__init__(name, age)
        self.breed = breed

    def __str__(self):
        """Return a string representation of the Dog"""
        if self.breed:
            return f"{self.name} is a {self.breed} and is {self.age} years old"
        return super().__str__()

    def make_sound(self):
        """Override the parent's make_sound method"""
        return self.speak()

    def speak(self, sound="Woof"):
        """Let the dog speak

        Args:
            sound (str): The sound the dog makes (default: "Woof")

        Returns:
            str: The dog's message
        """
        return f"{self.name} says {sound}"


# Example usage
if __name__ == "__main__":
    # Create an instance of the base Animal class
    leo = Animal("Leo", 4)
    print(leo)                 # Output: Leo is 4 years old
    print(leo.make_sound())    # Output: Leo makes a sound
    print(leo.birthday())      # Output: Leo is now 5 years old!
    print(f"Kingdom: {leo.kingdom}")  # Output: Kingdom: Animalia

    print("\n" + "-" * 30 + "\n")

    # Create instances of the Dog class
    fido = Dog("Fido", 3, "Beagle")
    bella = Dog("Bella", 5)

    # Access instance attributes
    print(fido.name)       # Output: Fido
    print(bella.age)       # Output: 5
    print(fido.breed)      # Output: Beagle

    # Access class attributes from both parent and child
    print(fido.species)    # Output: Canis familiaris
    print(fido.kingdom)    # Output: Animalia

    # Call instance methods
    print(fido.speak())                # Output: Fido says Woof
    print(bella.speak("Bark"))         # Output: Bella says Bark
    # Output: Fido says Woof (overridden method)
    print(fido.make_sound())

    # String representation (overridden)
    print(fido)            # Output: Fido is a Beagle and is 3 years old
    print(bella)           # Output: Bella is 5 years old

    # Inherited method
    print(fido.birthday())  # Output: Fido is now 4 years old!
