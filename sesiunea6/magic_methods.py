class Dog:
    species = 'mammal'

    def __init__(self, age, name):                  # instance attribute (constructor)
        self.age = age                              # proprietatiile clasei - pentru obiectul care va fi creat cu clasa Dog
        self.name = name                            # proprietatiile clasei - pentru obiectul care va fi creat cu clasa Dog

    def __str__(self):                              # returneaza un strig care e citibil
        return f'age:{self.age}, name:{self.name}'

    def __repr__(self):                             # folosit pentru printarea colectiilor de obiecte (ex: liste)
        return str(self)                            # sau: self.__str__() -> nu se foloseste asa des

    def __eq__(self, other):                        # verifica gradul de egalitate intre obiecte
        if not isinstance(other, Dog):
            return False
        return self.age == other.age and self.name == other.name

d = Dog(5, 'Rex')
print(f'Print object d: {d}')
print(f'Print name: {d.name}')              # printeaza proprietatea salvat in obiecul d -> name
print(f'Print age: {d.age}')                # printeaza proprietatea salvat in obiecul d -> age
# Modify Object Properties
d.age = d.age + 1                           # modifica proprietatea salvata in obiecul d -> age
print(f'Print new age value: {d.age} \n')   # printeaza noua valoare

d2 = Dog(4, 'Puffy')
print(d2)

d3 = Dog(4, 'Puffy')
print(d3)

lst = [d2, d]
print(lst)


print(d == d2)
print(d2 == d2)
print(d2 == d3)
print(d2 == 5)
