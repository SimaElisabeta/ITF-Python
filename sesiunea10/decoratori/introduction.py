# 1. Functie ca argument
def say_hello(name):
    print(f'Hello {name}')


def say_hi(name):
    print(f'Hi {name}')


def greet_bob(greater_func):
    greater_func('Bob')


greet_bob(say_hello)
greet_bob(say_hi)


# 2. Inner Functions = Functii interioare
def parent():
    print('Printing from parent() function')

    def first_child():
        print('Printing from first_child() function ')

    def second_child():
        print('Printing from second_child() function ')

    second_child()
    first_child()


parent()
print()


# 3. Returnare de functii
def parent(num):
    def first_child():
        print('Printing from first_child() function ')

    def second_child():
        print('Printing from second_child() function ')

    if num == 1:
        return first_child
    else:
        return second_child


f = parent(1)       # f -> referinta catre functia first_child()
print(type(f))      # f este o functie
f()                 # f() -> va apelia functia first_child()
