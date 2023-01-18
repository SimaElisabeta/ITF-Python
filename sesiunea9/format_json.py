# json = Javascript Object Notation
import json
from pprint import pprint


def read(file_name):
    with open(file_name, "r") as f:
        return json.load(f)


e = read("employees.json")
pprint(e)


def write(file_name, data):
    with open(file_name, "w") as f:
        json.dump(data, f, indent=4)


data = [
    {"Nume": "Sergiu", "Varsta": "24"},
    {"Nume": "Andrei", "Varsta": "31"},
    {"Nume": "Dan", "Varsta": "22"},
    {"Nume": "Ioana", "Varsta": "20"}
]

write('persons.json', data)
