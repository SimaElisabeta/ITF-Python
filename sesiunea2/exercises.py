# 1. sa se scrie un program care citeste un text de la tastatura
# si verifica daca are lungimea par sau impar ( rezolvare in 2 moduri)

# rezolvare 1: varianta mai lunga, aceeasi rezolvare
text = input('Introdu un text: ')
if len(text) % 2 == 0:
    print('lungimea textului este par')
else:
    print('lungimea textului este impar')


# rezolvare 2: shorthand (prescurtare)
paritate = 'par' if len(text) % 2 == 0 else 'impar'
print(f'lungimea textului este {paritate}')



# 2. se citesc 2 numere de la tastatura,
# sa se afiseze cuvantul adevarat daca ambele numere au acelasi semn
# altfel se afiseazacuvantul fals

x = int(input('Introdu un numar: '))
y = int(input('Introdu un numar: '))

if (x > 0 and y > 0) or (x < 0 and y < 0):
    print('Adevarat')
else:
    print('False')