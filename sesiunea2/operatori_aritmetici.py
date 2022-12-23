# operatorii aritmetici dau un tip de date int
x = 15
y = 5

print('x + y =', x + y)
print('x - y =', x - y)
print('x * y =', x * y)         # se inmulteste
print('x ** y =', x ** y)       # ** ridica la putere
print('nr real -> x / y =', x / y)         # / slash => impartire reala
print('nr natural -> x // y =', x // y)       # // slash => impartire naturala (fara partea de zecimala)
z = x // y
g = x / y
print(type(z), z)
print(type(g), g)

print('x % y =', x % y)         # restul impartirii

# !! de retinut !!
# functioneaza si asa:
# mai multe operatii intr-o linie
print(x + y + 5)