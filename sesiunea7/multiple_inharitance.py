class Car:

    def go(self):
        print('Vrum, vrum')

    def start(self):
        print('Starting car.')


class Flyable:
    def fly(self):
        print('Flu, flu')

    def start(self):
        print('Starting flyable.')


class FlyingCar(Car, Flyable):
    pass


fc = FlyingCar()
fc.fly()
fc.go()
fc.start()  # MRO - method resolution order -> se decide care functie din clasa Car sau Flyable se va apela (de la stanga la dreapta)


class FlyingCar2(Car, Flyable):
    def start(self):
        Car.start(self)
        Flyable.start(self)


fc2 = FlyingCar2()
fc2.start()
