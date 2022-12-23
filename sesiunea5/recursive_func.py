# functia recursiva este o functie care se apeleaza pe ea insasi
# Fibonacci: 0 1 1 2 3 5 8 13 21

def recursive_fibonacci(n):
    if n <= 1:
        return n
    else:           # nu ar mai fi nevoie de else, doarece avem un if cu return
        return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

for i in range(10):
    print(recursive_fibonacci(i))


def suma_primelor_n_numere(n):
    if n == 0:
        return 0
    return n + suma_primelor_n_numere(n-1)

print(suma_primelor_n_numere(50))
print(sum(range(51)))