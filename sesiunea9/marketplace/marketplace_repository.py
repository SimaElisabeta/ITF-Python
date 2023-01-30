import csv
import json
from abc import ABC, abstractmethod


class EntityNotFoundException(Exception):
    pass


class AbstractMarketplaceRepository(ABC):

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def add(self, entity):
        pass

    @abstractmethod
    def delete(self, entity_id):
        pass


class CSVMarketplaceRepository(AbstractMarketplaceRepository):
    def __init__(self, file_name):
        self.file_name = file_name
        self.data = None

    def read(self):
        if self.data:  # checks if the data attribute is set and will return the data
            return self.data
        # else if the data is not set than it will open the specified file 'file_name' in read mode
        # and reads the data in the file using the 'csv.reader'.
        # In the end, all data that has been read will be assigned to data attribute and returned
        with open(self.file_name, "r") as f:
            reader = csv.reader(f)
            self.data = list(reader)
            return self.data

    def add(self, entity):
        with open(self.file_name, "a", newline='') as f:  # opens the file with 'a' - append mode
            writer = csv.writer(f)
            writer.writerow(entity)
            self.data = None  # invalidam datele locale pentru ca s-a modificat fisierul
            # 1. self.data = None - determina faptul ca datele noastre nu sunt actualizate iar cand vom folosi functia
            # read() acesta va merge direct catre open si va citi(+ va salva in read mode) fisierul actualizat
            # 2. daca nu invalidam datele atunci cand vom incerca sa citim ce este in fisier, functia read()
            # ne va returna doar datele care erau inainte de a modifica/adauga in fisier

    def delete(self, entity_id):
        self.data = self.read()
        changed = False
        for elem in self.data:
            if elem[0] == entity_id:
                changed = True
                self.data.remove(elem)
        if not changed:
            raise EntityNotFoundException(f'Entity with ID: {entity_id} not found!')
        with open(self.file_name, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(self.data)


class JSONMarketplaceRepository(AbstractMarketplaceRepository):
    def __init__(self, file_name):
        self.file_name = file_name
        self.data = None

    def read(self):
        if self.data:
            return self.data
        with open(self.file_name, 'r') as f:
            try:
                self.data = json.load(f)
            except:
                self.data = []
            return self.data

    def add(self, entity):
        with open(self.file_name, 'w') as f:
            self.data = self.read()
            self.data.append(entity)
            json.dump(self.data, f, indent=4)

    def delete(self, entity_id):
        self.data = self.read()
        changed = False
        for elem in self.data:
            if str(elem.get("ID")) == entity_id:
                changed = True
                self.data.remove(elem)
        if not changed:
            raise EntityNotFoundException(f'Entity with ID: {entity_id} not found!')
        with open(self.file_name, 'w') as f:
            json.dump(self.data, f, indent=4)
