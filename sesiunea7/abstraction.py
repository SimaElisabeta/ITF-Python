# O clasa abstracta, este o clasa care are cel putin 1 metoda abstracta.
# O metoda abstracta este o metoda fara corp (apre doar pass in interior, corp = ce este inauntrul functiei).
# O clasa abstracta nu poate fi instantiata.
# METODA ESTE FUNCTIA DINTR-O CLASA! DE retinut!!!

from abc import abstractmethod, ABC  # Abstract Base Class


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def sleep(self):
        raise NotImplementedError


class Dog(Animal):
    def sound(self):
        print('Ham, ham')

    def sleep(self):
        print('Zzzz, zz')


class Cat(Animal):

    def sound(self):
        print('Miau, miau')

    def sleep(self):
        print('Prrrrr')


cat1 = Cat()
dog1 = Dog()

cat1.sound()
cat1.sleep()

dog1.sound()
dog1.sleep()

# a = Animal()            # -> EROARE pentru ca nu se poate instantia o clasa abstracta
# a.sleep()
