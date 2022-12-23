print(20 * '-', 'example of functions', 20 * '-')
def say_hi(name):       # name -> parameter (denumirea variabilei)
    print(f'Hi, {name}')
say_hi('Adrian')
say_hi('Adriana')


def show_sum(a, b):
    print(a + b)
show_sum(7, 5)


def show_dict(dct):
    print(dct)
show_dict({'abc': 123})