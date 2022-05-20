from django.db import models
from django.utils import timezone

# Create your models here.

class Animal(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)

class Breed(models.Model):
    id = models.AutoField(primary_key=True)
    breedName = models.CharField(max_length=128)
    name = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='breed')

class AnimalData(models.Model):
    id = models.AutoField(primary_key=True)
    animalname = models.CharField(max_length=128)
    breedname = models.CharField(max_length=128)
    created = models.DateTimeField(editable=False,default=timezone.now)

class empty(models.Model):
    pass
