# How do we store a single value?
# variable

# Several values?
# list

# Details about a single value?
# dictionary

# Repeat a piece of code, indefinitely?
# while loop

# Work through a list?
# for loop

# Repeat a piece of "configurable" code, returning a value?
# function!!!!


# Classes are for:
# bundling related data (like a dictionary)
# with the functions that modify that data

from random import randint

class Cat:
    # In __init__ python allows you to
    # refer to the object as it's being created!
    # Cool! You can customize that cat. Prrrrrr....
    def __init__(self, new_name, friendliness=0.5, happiness=10, cuddle_power=3):
        self.name = new_name
        self.friendliness = friendliness
        self.happiness = happiness
        self.cuddle_power = cuddle_power

    def greet(self, whom):
        print(f"Hello, I am {self.name}. Nice to meet you, {whom.name}!")

    def cuddle(self, whom):
        cuddle_chance = randint(0, 10)/10
        if cuddle_chance <= self.friendliness:
            print(f"I cuddle you, {whom.name}!")
            whom.happiness += self.cuddle_power
        else:
            print(f"Bad touch, bad touch!")

milla = Cat("Milla")
oakley = Cat("Oakley") 
# Use the class to create a new Cat "instance"
# "Instance" is another word for "object"

