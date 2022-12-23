# Use the __init__() function to assign values to object properties, or other operations
# that are necessary to do when the object is being created:
# Note: The __init__() function is called automatically every time the class is being used to create a new object.

class Dog:
    species = 'mammal'

    def __init__(self, age, name):              # instance attribute (constructor)
        self.age = age
        self.name = name

    def bark(self):                             # self -> reference to the current object
        print('Ham,ham')

    def get_owner(self):
        return f'Eu sunt {self.name} si ma detine Andrei'


dog = Dog(3, 'Rex')
dog.bark()
print(dog.get_owner())

dog2 = Dog(3, 'Mimi')
print(dog2.get_owner())
print(type(dog))
print(type(Dog))
print(type(int))
