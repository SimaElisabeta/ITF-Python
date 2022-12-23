# lists are used to store multiple items in a single variable
# list items are ordered, changeable, and allow duplicates

# create
fruits = ['apple', 'banana', 'cherry']
numbers = [1, 2, 3, 4, 5]
cars = list(('BMW', 'Audi', 'Tesla'))

# indexing - accessing elements
print(20 * '-', 'indexing', 20 * '-')
print(numbers[0])
print(numbers[-1])
print(numbers[2:4])
print(numbers[::2])
print(numbers[::-1])        # inversare, ultimul pas => -1

# add element
print(20 * '-', 'add element', 20 * '-')
numbers.append(10)          # append - adds an element at the end on the list
print(numbers)
numbers.insert(4, 6)        # append - adds an element at a specific index, index = 4, append = 6
print(numbers)


# remove elements
print(20 * '-', 'remove element', 20 * '-')
elem = numbers.pop()        # removes the last element and returns it
print(elem)
print(numbers)

numbers.pop(0)              # removes first element from index 0
print(numbers)

numbers.remove(3)           # removes from my list the first element that has the value 3
print(numbers)


# remove all elements
print(20 * '-', 'remove all elements', 20 * '-')
numbers.clear()             # removes all elements from my list
print(numbers)

numbers = [1, 2, 3, 4, 5]


# replace
print(20 * '-', 'replace', 20 * '-')
fruits[1] = 'pear'
print(fruits)


# count
print(20 * '-', 'count', 20 * '-')
print(numbers.count(3))

# add two lists
print(20 * '-', 'add two lists', 20 * '-')
numbers2 = [10, 11, 12]
print(numbers + numbers2)       # creates a new list with all the elements from the lists
print(numbers)
numbers.extend(numbers2)
print(numbers)


# reverse
print(20 * '-', 'reverse', 20 * '-')
print(numbers[::-1])    # creaza o lista noua pe care nu o prescrie
numbers.reverse()       # in place, reverse modifica lista initiala
print(numbers)


# sort
print(20 * '-', 'sort', 20 * '-')
numbers = [5, 10, 8, 3, 0, 14]
numbers.sort()      # in place, ne modifica lista initiala
print(numbers)
numbers.sort(reverse=True)
print(numbers)


