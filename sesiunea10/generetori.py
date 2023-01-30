# generatorii sunt functii care implementeaza mecanismul iterator

def gen_even(n):
    generated_numbers = 0
    current_number = 0
    while generated_numbers < n:
        if current_number % 2 == 0:
            print(f'found: {current_number}')
            generated_numbers += 1
            yield current_number  # yield(cedeaza) - yield returneaza o valoare -> dupa ce aceasta nu mai este folosita, se va intoarce in functie sa execute codul in contiunare
        current_number += 1
        print('going to next number')


for i in gen_even(10):
    print(f'current i from yield = {i}')
    print('going back to next line code where we left from our function()...')
