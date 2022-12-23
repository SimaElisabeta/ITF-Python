"""sa se scrie un program care citeste un text de la tastatura si afiseaza o lista cu fiecare caracter in ordinea
inversa a aparitiei in text """

# text = list(input('Sa se scrie un text: '))
# text.reverse()
# print(text)
# chrs = [text.pop(-2), text.pop(7)]
# print(chrs)
# print(text)

""""
Sa se scrie un program care citeste numele, email si varsta unei persoane de la tastatura si adauga datele
intr-un dictionar pe care il afiseaza. Daca persoana nu este multumita cu datele introduse va putea specifica
daca vrea sa modifice maxim 1 valoare din dictionar.
"""
#
# nume = input('Numele: ')
# email = input('Email: ')
# varsta = int(input('Varsta: '))
#
# details = {
#     'nume': nume,
#     'email': email,
#     'varsta': varsta
# }
#
# print(details)
#
# modify = input('Vrei sa modifici datele (Y/N)? ')
# if modify == 'Y':
#     key_to_modify = input('Introdu ce vrei sa modifici: ')
#     if key_to_modify not in details:
#         print('Nu exista aceasta valoare')
#         exit(0)
#     value_to_modify = input('Introdu noua valoare: ')
#     value_to_modify = int(value_to_modify) if key_to_modify == 'varsta' else value_to_modify
#     details[key_to_modify] = value_to_modify
#
# print(details)


""""
Fie seturile s1, s2: 
a. toate elementele care apar in set1 si nu apar in set2
b. toate elementele care apar in ambele seturi
c. toate elementele care nu sunt comune
"""

set1 = {'yellow', 'orange', 'black'}
set2 = {'orange', 'blue', 'pink'}

print(set1 - set2)
print(set1 & set2)
print(set1 ^ set2)
