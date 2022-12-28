"""
3 tipuri de metode si atribute:
    * Public -> accesibile peste tot
    * Protected -> accesibile doar in ierarhia de mostenire (ele se vor nota _atribut)
    * Private -> accesibil doar in clasa (ele se vor nota cu __atribut)
"""

class Car:
    __model = 'Dacia'

    def get_model(self):                    # getter to obtain the model
        return self.__model

    def set_model(self, new_model):         # setter to update the current model
        self.__model = new_model


c = Car()
print(c.get_model())
c.set_model('Audi')
print(c.get_model())


################################################################################################
# properties(getter, setter, deleter)

class Car:
    def __init__(self, color):
        self.__color = color

    @property
    def color(self):
        print('Setting as property')
        return self.__color

    @color.getter
    def color(self):
        print('Getting value')
        return self.__color

    @color.setter
    def color(self, value):
        print('Setting color')
        self.__color = value

    @color.deleter
    def color(self):
        print('Deleting value.')
        self.__color = None


c = Car('blue')
print(c.color)
c.color = 'red'
print(c.color)
