# with the while loop, we can execute a set of statements as long as a condition is true

count = 0

while count < 3:
    count += 1
    print(f'count: {count}')

l = [1, 2, 3, 4, 5]
index = 0

while len(l) > index:
    print(l[index])
    index += 1



# break
print(20 * '-', 'break', 20 * '-')

i = 1

while i < 6:
    print(i)
    if i == 3:
        break                   # stops the iteration
    i += 1



# continue
print(20 * '-', 'continue', 20 * '-')

i = 1

while i < 6:
    i += 1
    if i == 3:
        continue                # skips the code bellow
    print(i)



# else
print(20 * '-', 'else', 20 * '-')

count = 0

while count < 3:
    count += 1
    print(count)
else:                           # runs when the loop else
    print('in else block')


# else + break
print(20 * '-', 'else + break', 20 * '-')
count = 0
while count < 3:
    count += 1
    print(count)
    if count == 1:
        break
else:                           # does not run when a break happened in the loop
    print('in else block')
