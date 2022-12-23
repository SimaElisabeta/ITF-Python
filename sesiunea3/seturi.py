# sets are used to store multiple unique items in a single variable (nu adauga duplicate si nu are ordine, le adauga aleatoriu!)

# create
fruits = {'apple', 'banana', 'cherry'}
# cars = {}         # atentie, acesta este un dictionar gol!
car = set()         # asa se creaza un set gol

# add elements
print(20 * '-', 'add elements', 20 * '-')
fruits.add('pear')
print(fruits)
fruits.add('pear')
print(fruits)

tropical = {'papaya', 'mango'}
fruits.update(tropical)
print(fruits)


my_list = ['kiwi', 'orange']
fruits.update(my_list)
print(fruits)


# remove elements
print(20 * '-', 'remove elements', 20 * '-')

fruits.remove('mango')
print(fruits)
fruits.discard('pear')
print(fruits)
# fruits.remove('greapes') - can't eliminate elements not in set
fruits.discard('greapes')
print(fruits)
fruits.pop()        # eliminates/removes a random element
print(fruits)
a = fruits.pop()
print(a)


# remove all elements
print(20 * '-', 'remove all elements', 20 * '-')

a = {1, 2, 2}
a.clear()
print(a)

# join elements
print(20 * '-', 'join elements', 20 * '-')
s1 = {'a', 'b', 'c'}
s2 = {1, 2, 3}
s3 = s1.union(s2)
print(s3)
print(s1|s2)        # | => operator pentru union


# intersection
print(20 * '-', 'intersection', 20 * '-')
x = {'apple', 'banana', 'cherry'}
y = {'google', 'Microsoft', 'apple'}
z = x.intersection(y)
print(z)
print(x & y)                # semnul pentru intersectie


# difference
print(20 * '-', 'difference', 20 * '-')
x = {'apple', 'banana', 'cherry'}
y = {'google', 'Microsoft', 'apple'}
z = x.difference(y)         # afiseaza elementele (unice) care sunt in x si nu sunt in y
print(z)
print(x - y)                # semnul pentru difference


# symmetric difference
print(20 * '-', 'symmetric difference', 20 * '-')
x = {'apple', 'banana', 'cherry'}
y = {'google', 'Microsoft', 'apple'}
z = x.symmetric_difference(y)   # printeaza toate elementele care nu sunt comune (le scoate pe cele comune)
print(z)
print(x ^ y)                    # semnul pentru difference


# issubset, issuperset
print(20 * '-', 'issubset, issuperset', 20 * '-')
a = {1, 2, 3, 4, 5}
b = {1, 2, 3}

print(b.issubset(a))        # verifica daca toate elementele din be se afla si in a
print(a.issuperset(b))      # verifica daca a cotine toate elementele lui b




