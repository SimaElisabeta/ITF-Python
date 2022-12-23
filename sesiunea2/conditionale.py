# if = daca; else = altfel

# 1. if

a = 33
b = 200
if b > a:
    print('b greater than a')

if False:
    print('linia aceasta nu se executa')


# 2. if ... else
a = 330
b = 200
if b > a:
    print('b greater than a')
else:
    print('b smaller than a')


# 3. if ... elif ... else
a = 1
b = -1

if b > a:
    print('b greater than a')
elif b == a:
    print('b equals a')
elif b == 0:
    print('b equals 0')
else:
    print('b smaller than a')


# 4. shorthand (prescurtare)
a = 2
b = 33

print('a') if a > b else print('b')
c = a if a < b  else b


# varianta extinsa a liniei 42:
if a < b:
    c = a
else:
    c = b
