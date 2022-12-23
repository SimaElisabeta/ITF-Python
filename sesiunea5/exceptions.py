# exceptions are events that might happen during the execution of a code that python does not know how to treat
# (exceptiile sunt evenimente care s-ar putea intampla in timpul executiei unei bucati de cod pe care python nu stie cum sa le trateze)

try:                    # tests a block of code for errors
    print(x)
except:                 # treats different types of errors
    print('A aparut o eroare')


########################################################################################################
try:
    print(x)
    # a = 1/0
    # l=[1, 2, 3]
    # l.add(5)
except NameError:
    print('A aparut NameError')
except AttributeError as ex:            # as ex: -> stocheaza eroarea si o printeaza
    print(f'Eroare: {ex}')
except:
    print('Alt tip de eroare.')


########################################################################################################
try:
    print('Hello')
except:
    print('A aparut o eroare')
else:                           # executes if there was no error
    print('Nici o eroare')


########################################################################################################
try:
    print('x')
except:
    print('A aparut o eroare')
finally:
    print('Finished')           # always executes at the end


########################################################################################################
x = int(input('Intordu un numar: \n'))
if x < 0:
    raise Exception(f'{x} is bellow 0')


########################################################################################################
"""
try: (Blocul try)
    bloc de cod unde ar putea aparea o eroare
    (Sfarsitul blocului try)
except NumeEroare: <-- Prinderea tuturor exceptiilor de tipul NumeEroare
    se executa doar daca se prinde NumeEroare
except (AltNumeEroare, IncaUnNumeEroare): <-- Gruparea mai multe tipuri de Exceptii
    se executa daca se prinde AltNumeEroare sau IncaUnNumeEroare
except Eroarea4 as ex: <-- Stocarea mesajului unei erori intr-o variabila (exemplul variabilei 'ex')
    se poate accesa mesajul de Eroarea4 prin variabila ex
except:
    se executa la orice alt tip de eroare nespecificat
else:
    se executa doar daca nu se arunca eroare in blocul try
finally:
    se executa indiferent daca se arunca eroare sau nu
"""

