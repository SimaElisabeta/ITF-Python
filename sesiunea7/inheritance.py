class Person:

    def __init__(self, age, name):
        self.age = age
        self.name = name

    def print_name(self):
        print(f'My name is {self.name}')

class Student(Person):

    def __init__(self, age, name, university):
        # Person.__init__(self, age, name)          # var 1
        super().__init__(age, name)                 # var 2
        self.university = university

    def print_name(self):                           # suprascrie (aceeasi) -> functia definita in clasa Person
        print(f'My name is {self.name}, and I study at {self.university}')

s1 = Student(18, 'John', 'UCLA')
print(s1.age)
s1.print_name()
