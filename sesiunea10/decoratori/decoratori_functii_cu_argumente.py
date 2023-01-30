import functools


def do_twice(func):
    @functools.wraps(func)
    def wrapper(*arg, **kwargs):
        func(*arg, **kwargs)
        func(*arg, **kwargs)

    return wrapper


@do_twice
def say_hello(name):
    print(f'hello {name}')


say_hello('Bob')
print()


def do_twice_again(func):
    @functools.wraps(func)
    def wrapper(*arg, **kwargs):
        func(*arg, **kwargs)
        return func(*arg, **kwargs)  # returnam functia ca sa o putem printa, daca nu returnam nimic atunci vom primi None

    return wrapper


@do_twice_again
def greet(name):
    return f'Hello {name}'  # daca in functie avem un return, atunci si la wrapper trebuie sa returnam functia


# g = greet('Bob')
# print(g)
print(greet('Bob'))



