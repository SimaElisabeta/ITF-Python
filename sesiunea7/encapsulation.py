"""
3 tipuri de metode si atribute:
    * Public -> accesibile peste tot
    * Protected (_) -> accesibile doar in ierarhia de mostenire (ele se vor nota _atribut)
    * Private (__) -> accesibil doar in clasa (ele se vor nota cu __atribut)
"""


################################################################################################
# Varianta 1
# getter si setter -> specific pentru mai multe limbaje

class Car:
    __model = 'Dacia'

    # variabila __model nu se poate accesa in afara clasei deoarece este Private
    # pentru a accesa, vom crea atribute speciale: getter si setter

    def get_model(self):  # getter -> to obtain the model
        return self.__model

    def set_model(self, new_model):  # setter -> to update the current model
        self.__model = new_model


c = Car()
print(c.get_model())
c.set_model('Audi')
print(c.get_model())


################################################################################################
# Varianta 2
# properties (getter, setter, deleter) -> specific python

class Car:
    def __init__(self, color):
        self.__color = color

    @property
    def color(self):    # functia def color(self), va seta culoarea ca si o proprietate
        print('Setting as property')
        return self.__color

    @color.getter       # setam functia de setter
    def color(self):
        print('Getting values')
        return self.__color

    @color.setter       # setam functia de getter
    def color(self, value):
        print('Setting color')
        self.__color = value

    @color.deleter      # setam functia de deleter
    def color(self):
        print('Deleting value')
        self.__color = None


c = Car('Blue')
print(f'Printeaza culoarea: {c.color} \n')
c.color = 'Red'
print(f'Printeaza culoarea: {c.color} \n')
del c.color
print(f'Printeaza culoarea: {c.color} \n')
