# 1. Implementati diagrama de clase
# 2. Fie functia ride() care afisieaza numele ownerului si tipul vehicului sub forma de:
# nume owner rides a tip vehicol

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Vehicle:
    def __init__(self, vehicle_type, capacity, power, owner):
        self.type = vehicle_type
        self.capacity = capacity
        self.power = power
        self.owner = owner

    def ride(self):
        print(f'{self.owner.name} rides a {self.type}.')


class UtilityVehicle(Vehicle):
    def __init__(self, capacity, power, owner, load_capacity):
        super().__init__('utility_vehicle', capacity, power, owner)
        self.load_capacity = load_capacity


class Car(Vehicle):
    def __init__(self, capacity, power, owner, fuel_type):
        super().__init__('car', capacity, power, owner)
        self.fuel_type = fuel_type


class Bike(Vehicle):
    def __init__(self, capacity, power, owner):
        super().__init__('bike', capacity, power, owner)


class Bus(Car):
    def __init__(self, capacity, power, owner, fuel_type, passengers_type):
        super().__init__(capacity, power, owner, fuel_type)
        self.passengers_type = passengers_type


class MotorBike(Bike):
    def __init__(self, capacity, power, owner, engine_capacity):
        super().__init__(capacity, power, owner)
        self.engine_capacity = engine_capacity


# 3. Fie lista de vehicule:

p1 = Person("Sergiu", 24)
p2 = Person("Valentina", 23)

VEHICLES = [
    Car(capacity=5, power=90, owner=p1, fuel_type="benzina"),
    Car(capacity=5, power=105, owner=p2, fuel_type="benzina"),
    Car(capacity=5, power=60, owner=p1, fuel_type="motorina"),
    Bus(capacity=40, power=150, owner=p2, fuel_type="motorina", passengers_type="elevi"),
    Bus(capacity=35, power=150, owner=p1, fuel_type="motorina", passengers_type="angajati"),
    Bike(capacity=1, power=5, owner=p1),
    MotorBike(capacity=1, power=80, owner=p2, engine_capacity=500),
    MotorBike(capacity=1, power=75, owner=p1, engine_capacity=250),
    UtilityVehicle(capacity=1, power=200, owner=p1, load_capacity=90),
    UtilityVehicle(capacity=1, power=150, owner=p2, load_capacity=100),
]


# 3.a -> Sa se scrie o functie care primeste ca parametru o lista de vehicule si apeleaza functia ride() pt fiecare

def vehicles_ride(vehicles):
    for vehicle in vehicles:
        vehicle.ride()


vehicles_ride(VEHICLES)


# 3.b - Sa se scrie o functie, care returneaza toate vehiculele cu o capacitate mai mult de 2 persoane

def get_all_with_more_than_2_seats(vehicles):
    more_than_2_seats = []
    for vehicle in vehicles:
        if vehicle.capacity > 2:
            more_than_2_seats.append(vehicle)
    return more_than_2_seats


print(get_all_with_more_than_2_seats(VEHICLES))


# 3.c - Sa se scrie o functie, care returneaza toate numele persoanelor care detin o clasa 'Bike'

def get_all_bikers_names(vehicles):
    all_bikers_names = set()
    for vehicle in vehicles:
        if isinstance(vehicle, Bike):
            all_bikers_names.add(vehicle.owner.name)
    return list(all_bikers_names)


print(get_all_bikers_names(VEHICLES))
