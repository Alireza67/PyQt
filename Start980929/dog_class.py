
class Dog():
    """A simple Model from a dog"""

    def __init__(self, age, name):
        """initialize name and age attributes"""
        self.age = age
        self.name = name


    def sit(self):
        pass


    def roll_over(self):
        pass

first_sample = Dog(2, "Jack")

print("dog name is: ",first_sample.name)
print("It's age is: ", first_sample.age)