print(20 * '-', 'example of parameters and return functions', 20 * '-')

def produs(a, b):
    return a * b

p = produs(5, 6)
print(p)


def patratul_primelor_nr(n):
    result = []
    for i in range(n):
        patrat = produs(i, i)
        result.append(patrat)
    return result

print(patratul_primelor_nr(10))


def get_all_even_numbers(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

print(get_all_even_numbers([5, 7, 9, 18, 58, 43, 11, -13, 17, -18]))
