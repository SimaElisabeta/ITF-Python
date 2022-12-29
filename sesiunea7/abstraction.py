# O clasa abstracta, este o clasa care are cel putin 1 metoda abstracta.
# O metoda abstracta este o metoda fara corp (apre doar pass in interior, corp = interiorul functiei).
# METODA ESTE FUNCTIA DINTR-O CLASA! de retinut!!!
# O clasa abstracta nu poate fi instantiata (nu se pot crea obiecte din acceasta clasa, deoarece are metode care
# nu sunt implementate!).

# DE retinut!
# * Clasa abstracta forteaza anumite comportamente (implementarea unor metode) pentru toate clasele care o mostenesc!


from abc import abstractmethod, ABC  # ABC = Abstract Base Class


class Animal(ABC):
    @abstractmethod  # se va folosi (ca si conventie) decoratorul: @abstractmethod
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
