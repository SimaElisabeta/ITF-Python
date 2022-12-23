# a for loop is used for itereting over a sequence (sequence = list, tuple, dict, set, string)

print(20 * '-', 'for range 10', 20 * '-')

for i in range(10):     # 0 - 9
    print(i)



print(20 * '-', 'for range (1, 6)', 20 * '-')
for i in range(1, 6):   # 1 - 5
    print(i)



print(20 * '-', 'for i in list', 20 * '-')
lst = [1, 2, 3, 4, 5]

for i in range(len(lst)):
    print(lst[i])



print(20 * '-', 'range with step', 20 * '-')
for i in range(1, 6, 2):
    print(i)



print(20 * '-', 'reverse range', 20 * '-')
for i in range(5, 0, -1):
    print(i)



print(20 * '-', 'reverse list range', 20 * '-')
for i in range(len(lst)-1, -1, -1):         # start e continut, stop nu e continut
    print(lst[i])



# for each
print(20 * '-', 'for each', 20 * '-')

fruits = ['apple', 'banana', 'cherry']

for fruit in fruits:
    print(fruit)


print(20 * '-', 'for each in string', 20 * '-')
for x in 'Ana are mere':
    print(x)


# for each in dict
print(20 * '-', 'or each in dict', 20 * '-')
dct = {'a': 1,
       'b': 2}

for x in dct:           # in a dict, you iterate through keys
    print(x)
    print(dct[x])

for key, value in dct.items():
    print(key, value)


# break in for
print(20 * '-', 'break in for', 20 * '-')

for x in fruits:
    print(x)

    if x == 'banana':
        break


# continue in for
print(20 * '-', 'continue in for', 20 * '-')

for x in fruits:
    if x == 'banana':
        continue
    print(x)


# else in for
print(20 * '-', 'else in for', 20 * '-')

for x in range(10):
    print(x)
else:
    print('finally finished')


# nested in for
print(20 * '-', 'nested in for', 20 * '-')

adj = ['red', 'big', 'tasty']

for fruit in fruits:                # nu e ok sa folosim prea des for in for!
    for x in adj:
        print(x, fruit)


# pass in for
print(20 * '-', 'pass in for', 20 * '-')

for x in [1, 2, 3]:
    pass