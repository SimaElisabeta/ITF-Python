# variable -> a container from memory for storing values
# in python putem rescrie o variabila atribuindui un alt tip de date


# 1. creating a variable

x = 5
y = 'John'

print(x)
print(y)

x = y
print(x)



# 2. naming a variable

'''
a) a variable must start with a letter or the underscire character: _
b) a variable cannot start with a number
c) a variable name can only contain alpha-numeric characters and _ (A-Z, a-z, 0-9, _)
d) a variable names are case-sensitive
'''

# YES this way:
myVar = 5
my_var = 5
my_var2 = 5
_myVar = 5
myvar = 5
MYVAR = 5

# NOT this way:
# 2myVar = 5
# my-var = 5
# my var = 5



# 3. Many values to multiple variable (multe valori la mai multe variabile) - in Java nu se poate face asa ceva, nu iti permite limbajul!
x, y, z = 1, 2, 3
print(x)
print(y)
print(z)

k, h, j = x, 'mere', True
print(k, h, j)




# 4. One value to multiple variables

x = y = z = 'portocala'
print(x, y, z)




