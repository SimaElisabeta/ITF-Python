from django.db import models

# Create your models here.
PET_GENDERS = [
    ('F', 'Female'),
    ('M', 'Male')
]

PET_TYPES = [
    ('cat', 'Cat'),
    ('dog', 'Dog'),
    ('rabbit', 'Rabbit')
]


class Pet(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=PET_GENDERS, null=False)
    species = models.CharField(max_length=6, choices=PET_TYPES)

    def __str__(self):
        return f'{self.name} -> {self.location} -> {self.gender} -> {self.species}'
