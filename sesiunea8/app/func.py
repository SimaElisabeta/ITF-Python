# Sa se scrie o functie care primeste ca parametru un intreg si returneaza:
# 35 daca numarul este divizibil cu 3 si cu 5
# 3 daca este divizibil cu 3
# 5 daca este divizibil cu 5

def is_div_3_5(n):
    if n % 3 == 0 and n % 5 == 0:
        return 35
    if n % 3 == 0:
        return 3
    if n % 5 == 0:
        return 5


# sa se scrie o functie care primeste ca parametru o lista si verifica
# daca toate elementele sunt intregi,
# daca nu, sa se arunce o exceptie custom

class NotIntegerNumberException(Exception):
    pass


def only_ints(numbers):
    for number in numbers:
        if not isinstance(number, int):
            raise NotIntegerNumberException(f'{number} is not an integer')