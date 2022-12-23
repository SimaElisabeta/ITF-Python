# operatorii speciali dau un tip de date bool

# 1. operatori de identitate:

x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'

print(x1 is y1)
print(x1 is not y1)


x3 = [1, 2, 3]
y3 = [1, 2, 3]
print(x3 == y3)
print(x3 is y3)         # pentru tipui de date complexe, is -> verifica daca cei doi operanzi sunt exact acelasi obiect

# is -> verifica pentru tipuri de date complexe daca este fix acelasi obiect


# 2. membership operators (operatori de apartenenta)
x = 'Ana are mere'
print('a' in x)         # verifica daca un element apartine valorii unei variabile
print('t' not in x)
