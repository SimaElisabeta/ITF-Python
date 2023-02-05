""" Singleton - is a creational design pattern that lets you ensure that a class has only one instance
while providing a global access point to this instance """


# Example 1
class SingletonLogger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print('Creating the SingletonLogger Object!')
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, file_name):
        if hasattr(self._instance, 'file_name'):  # verifica daca self.file_name este deja existent,
            return  # daca acesta exista deja atunci nu va mai returna noul atribut ci il va pasta pe primul creat
        self.file_name = file_name


logger = SingletonLogger('hello.txt')
print(logger.file_name)
logger2 = SingletonLogger('hello2.txt')
print(logger2.file_name)
print(logger.file_name)

print(logger)
print(logger2)
print()


# Example 2
class SingletonClass:
    __instance = None
    sector = 'IT'

    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance


a = SingletonClass('Andrei')
print(f'Printing a.name attribute: {a.name} ')
print('Creating a new instance of the SingletonClass with different attribute: ')
m = SingletonClass('Mihai')
print(f'Printing m.name attribute: {m.name} ')
print(
    f'If we call again a.name we get: {a.name}, because last instance of the class created, overwrote the first instance')
print()

print(f'Print m: {m}')
print(f'ID m: {id(m)}')
print(f'Print a: {a}')
print(f'ID a: {id(a)}')

"""
PROS:
    - you can be sure that a class has only a single instance
    - you can gain a global access point to that instance
    - the singleton object is initialized only when it's requested for the first time
CONS:
    - the singleton pattern can mask bad design, for instance: when the components of the program know too much about each other
"""
