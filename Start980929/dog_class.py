
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


    def change_age(self,age):
        self.age = age

first_sample = Dog(2, "Jack")
first_sample.change_age(4)
first_sample.age = 6

print("dog name is: ",first_sample.name.title())
print(first_sample.name.title()+"'s age is: ", first_sample.age, " years old.")