from abc import ABC, abstractmethod
from datetime import datetime


# Example 1
class Money(ABC):
    @abstractmethod
    def pay(self, s):
        pass


class Cash(Money):
    def __init__(self, amount, limit=10_000):
        self.amount = amount
        self.limit = limit

    def report(self, s):
        print(f'{datetime.now()} am cheltuit {s} lei si am mai ramas cu {self.amount} lei.')

    def pay(self, s):
        self.amount -= s
        self.report(s)


class Card(Money):
    def __init__(self, cash):
        self.cash = cash

    def amount_ok(self, s) -> bool:
        return s < self.cash.amount

    def limit_ok(self, s) -> bool:
        return s < self.cash.limit

    # def report(self, s):
    #     print(f'{datetime.now()} am cheltuit {s} lei si am mai ramas cu {self.cash.amount} lei.')

    def pay(self, s):
        if self.amount_ok(s) and self.limit_ok(s):
            self.cash.pay(s)
            # self.report(s)


cash = Cash(10_000, 2_000)
cash.pay(1_000)
print('*' * 60)
cash = Cash(10_000, 2_000)
card = Card(cash)
card.pay(900)
print('*' * 60)

# Example 2
NOT_IMPLEMENTED = "You should implement this!"


class AbstractCar:
    @abstractmethod
    def drive(self):
        raise NotImplementedError(NOT_IMPLEMENTED)


class Car(AbstractCar):
    def drive(self) -> None:
        print('Wroom, wroom...')
        print(f'Car has been driven by {driver.name}!')


class Driver:
    def __init__(self, age: int, name: str) -> None:
        self.age = age
        self.name = name


class ProxyCar(AbstractCar):
    def __init__(self, driver: any) -> None:
        self.car = Car()
        self.driver = driver

    def drive(self) -> None:
        if self.driver.age <= 18:
            print(f'Sorry, the driver {driver.name} is too young to drive.')
        else:
            self.car.drive()


driver = Driver(16, 'Alex')
car = ProxyCar(driver)
car.drive()
print('-' * 60)
driver = Driver(25, 'Mihai')
car = ProxyCar(driver)
car.drive()
