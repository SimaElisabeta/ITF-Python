# 1. Sa se scrie o functie care primeste oricati parametrii si de orice fel
# si returneaza lista valorilor argumentelor

print(20 * '-', 'Exercitiul 1', 20 * '-')

def get_list_all_parameters(*args, **kwargs):
    return list(args) + list(kwargs.values())

print(get_list_all_parameters(2, 8, -18, a=55))


# 2. Sa se scrie o functie care primeste ca parametrii o lista si returneaza inversul al acelei liste

print(20 * '-', 'Exercitiul 2', 20 * '-')
def get_list_reversed(lst):
    return lst[::-1]

print(get_list_reversed([1, 8, 13, 55, -14, 0]))


# 3. Sa se scrie o functie care primeste ca parametru 2 numere si il returneaza pe cel mai mare
print(20 * '-', 'Exercitiul 3', 20 * '-')
def get_max_between(a, b):
    return a if a > b else b

print(get_max_between(8, 0))
print(get_max_between(8, 10))


# 4. Sa se scrie o functie care primeste ca parametru o lista si un numar
# functia va returna de cate ori apare acel numar in lista
# iar daca nu apare deloc va arunca o eroare
print(20 * '-', 'Exercitiul 4', 20 * '-')
#
def get_count_in_list(lst, a):
    counter = lst.count(a)
    if not counter:
        raise Exception(f'{a} nu se afla in lista')
    return counter

print(get_count_in_list([1, 5, 8, 13, -14, 2, 15, 1, 16, 1], 0))

# 4.2. Sa se scrie o functie care primeste ca parametru o lista si un numar
# functia va returna de cate or apare acel numar in lista
# iar daca nu apare deloc va arunca o eroare.
# print(20 * '-', 'Exercitiul 4.2', 20 * '-')
# def get_count_in_list(lst, a):
#     counter = lst.count(a)
#     if not counter:
#         raise Exception(f'{a} nu se afla in lista.')
#     return counter
#
#
# print(get_count_in_list([1, 5, 8, 13, -14, 2, 15, 1, 16, 1], 1))


# 5. Sa se scrie o functie care citeste un string de la tastatura
# si returneaza toate caracterele folosite in acel string
print(20 * '-', 'Exercitiul 5', 20 * '-')

def get_unique_characters():
    exemplu = input('Scrie ceva frumos: \n')
    return list(set(exemplu))

print(get_unique_characters())


# 6. Sa se scrie o functie care citeste un string de la tastatura
# si returneaza toate caracterele folosite in acel string ordonate alfabetic
print(20 * '-', 'Exercitiul 6', 20 * '-')

def get_sorted_unique_char():
    chars = get_unique_characters()
    chars.sort()
    return chars

print(get_sorted_unique_char())