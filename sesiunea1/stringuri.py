name = 'Drago'

print(len(name))            # length of the string
print(len(name) // 2)       # length of the string, impartirea "//" imi va retruna un int
print(len(name) / 2)        # length of the string, impartirea "/" imi va retruna un float
print('')
print(name.upper())         # convert string to upper case
print(name.lower())         # convert string to lower case

name = 'Anamaria'
print(name.count('a'))      # counts the number of occurrences of the given character
print(name.count('s'))

prop = 'Oare vreau sa merg acolo! \nUnde sa merg!'      # \n = new line - scrie 2 linii despartite de enter
print(prop)
prop = prop.replace('!', '?')                           # replace all characters that contain ! with ?
print(prop)

food = 'pizza'
print(food.replace('zz', 't'))                          # replace all characters that contain zz with t


name = 'John'
print(name.index('o'))      # finds the index of the given character
print(name[0])
print(name[-1])             # traversare inversa a stringului - printeaza de la capat/mirroring (-1 este ultimul carcacter)

d = '0123456789'
print(d[2:5])               # from 2 to 5 (without 5) -> slicing            => 234
print(d[:5])                # from start to 5 (without 5)                   => 01234
print(d[2:])                # from 2 to end                                 => 23456789
print(d[-5:-2])             # from -5 to -2 (without 2)                     => 567
print(d[2:8:2])             # from 2 to 8 (without 8) with a pas of 2       => 246
