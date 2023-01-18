def read(file_name):
    f = open(file_name, 'r')  # r = mod deschidere fisier (read - citire)
    try:
        return f.readlines()
    except:
        print("Error reading file!")
    finally:
        f.close()  # se inchide accesul la fisier


def read_safe(file_name):
    with open(file_name, "r") as f:  # with - se ocupa automat de file.close()
        return f.readlines()


lines = read("data.txt")
lines2 = read_safe("data.txt")
print(lines)
print(lines2)


def write(file_name, data):
    with open(file_name, "w") as f:  # w = mod deschidere fisier (write - scriere)
        f.writelines(data)  # modul write suprascrie intregul fisier


write("data2.txt", ['1', '7', '3', '3', 'abc'])


def append(file_name, data):
    with open(file_name, "a") as f:  # a = mod deschidere fisier (append - adaugare)
        f.writelines(data)  # modul append va scrie in continuarea ultimului caracter din fisierului existent


append("data2.txt", ['6', '2', '0', 'NONE', 'abc'])
