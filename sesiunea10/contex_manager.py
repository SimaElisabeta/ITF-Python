# Pentru a implementa un conext manager, avem nevoie de o clasa care implementeaza functiile:
# * __enter__  -> deschide accesul la resurse si returneaza resursa
# * __exit__  -> inchide accesul la resurse

# Context manager - clasa
class FileManager:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
        self.f = None

    def __enter__(self):
        self.f = open(self.file_name, self.mode)
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()


with FileManager('data.txt', 'w') as f:
    f.write('Ana are mere si pere')


class HelloManager:
    def __enter__(self):
        print('Entering the context manager')
        return 'Hello world'

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Leaving the context manager')
        if exc_type == IndexError:
            print(f'Exception happend: {exc_val}')
        return True
        # cand __exit__ returneaza False - lasa eroarea sa se propage mai departe in cod (opreste executia urmatoarelor linii de cod)
        # cand __exit__ returneaza True - opreste eroarea si doar va printa (continua executia urmatoarelor linii de cod)


with HelloManager() as h:
    print(h)  # h -> return de la __enter__ (in cazul de fata returneaza stringul: 'Hello world')
    print(h[6])  # h[6] -> printeaza elementul de la indexul 6 (din stringul de sus)

    print(h[100])  # h[100] -> incearca sa acceseze elem de la index 100, acesta nu exista astfel va arunca o exceptie
    # (in cazul de fata va intra in if exc_type si printeaza ce avem in interior)
    print('this will not be printed')  # din cauza ca am avut eroare sus, tot ce se afla sub eroare nu se va mai printa

print('finally')
print()

#####################################################
# Context manager - functie
from contextlib import contextmanager


@contextmanager
def file_manager(file_name, mode):
    f = open(file_name, mode)
    yield f
    f.close()


with file_manager('data.txt', 'r') as f:
    print(f.read())

print()


@contextmanager
def hello_manager():
    print('Enter the context manager')
    yield 'Hello World Again'
    print('Leaving the context manager')


with hello_manager() as h:
    print(h)
