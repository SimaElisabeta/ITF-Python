# Polymorphism este conceptul care spune ca poti accesa obiecte de diferite tipuri prin aceeasi interfata

from abc import abstractmethod, ABC  # Abstract Base Class


class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name


class Creature(ABC):

    @abstractmethod
    def eat(self):
        pass


class Animal(Creature):
    def eat(self):
        return f'I am an eating {self.__class__.__name__}'

    def __init__(self, age, weight, species):
        self.age = age
        self.weight = weight
        self.species = species


class DomesticAnimal(Animal):
    def __init__(self, age, weight, species, owner):
        super().__init__(age, weight, species)
        self.owner = owner


class Pet(DomesticAnimal):
    def __init__(self, age, weight, species, owner, name):
        super().__init__(age, weight, species, owner)
        self.name = name


class WildAnimal(Animal):
    def __init__(self, age, weight, species, location):
        super().__init__(age, weight, species)
        self.location = location


p1 = Person("Sergiu", 24)
p2 = Person("Valentina", 23)
animals = [
    DomesticAnimal(age=5, weight=130, owner=p1, species="Cow"),
    Pet(name="Puffi", age=3, weight=4, owner=p2, species="Dog"),
    Pet(name="Pisu", age=1, weight=3, owner=p2, species="Cat"),
    Pet(name="Rexi", age=2, weight=3, owner=p1, species="Dog"),
    WildAnimal(age=25, weight=230, species="Bear", location="forest"),
    WildAnimal(age=18, weight=67, species="Wolf", location="forest"),
    WildAnimal(age=10, weight=59, species="Wolf", location="forest"),
    WildAnimal(age=40, weight=310, species="Elephant", location="jungle"),
    WildAnimal(age=33, weight=99, species="Giraffe", location="jungle"),
    DomesticAnimal(age=1, weight=2, owner=p1, species="Chicken"),
    DomesticAnimal(age=1, weight=145, owner=p2, species="Pig"),
    WildAnimal(age=2, weight=2, species="Squirrel", location="forest")
]


# sa se scrie o functie care primeste ca parametru o lista de animale si pentru fiecare apeleaza functia eat

def animals_eat(animals):
    for animal in animals:
        print(animal.eat())


animals_eat(animals)


# sa se scrie o functie care primeste ca parametru o lista de animale si returneaza doar animale domestice din acea lista

def get_all_domestic_animals(animals):
    domestic_animals = []
    for animal in animals:
        if isinstance(animal, DomesticAnimal):
            domestic_animals.append(animal)
    return domestic_animals


print(get_all_domestic_animals(animals))
