print(20 * '-', 'example of functions with return', 20 * '-')

def say_hi():
    return 'Hello!'     # terminates the execution of the function

text = say_hi()
print(text)


def print_first_50():
    for i in range(51):
        print(i)
    # return None / return -> is by default for every funcition


elem = print_first_50()
print(elem)