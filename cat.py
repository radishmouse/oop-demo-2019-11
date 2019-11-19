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

class Cat:
    # In __init__ python allows you to
    # refer to the object as it's being created!
    # Cool! You can customize that cat. Prrrrrr....
    def __init__(self, new_name):
        self.name = new_name

    def greet(self, whom):
        print(f"Hello, I am {self.name}. Nice to meet you, {whom.name}!")

    def cuddle(self, whom):
        pass

othercat = Cat("Milla")
mycat = Cat("Oakley") # Use the class to create a new Cat "instance"
                # "Instance" is another word for "object"