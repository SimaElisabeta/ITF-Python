import functools
from datetime import datetime


def my_decorator(func):
    def wrapper():
        print('Before the function is called')
        func()
        print('After the function is called')

    return wrapper


@my_decorator  # sintactic sugar => say_hello = my_decorator(say_hello)
def say_hello():
    print('Hello')


# say_hello = my_decorator(say_hello)
say_hello()
print()


# Sa se scrie un decorator care ruleaza o functie doar pe timp de noapte
def only_at_night(func):
    @functools.wraps(func)  # specificam ce functie este decorata
    def wrapper():
        h = datetime.now().hour
        if 18 < h < 24 or h < 8:
            func()

    return wrapper


@only_at_night  # say_hi = only_at_night(say_hi)
def say_hi():
    print('Hi!')
    print('Buna seara!')


say_hi()
print(say_hi)
