from django.http import HttpResponse
from django.shortcuts import render
from . models import *
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


def index(request):
    animals = Animal.objects.all()
    animalList = AnimalData.objects.all()
    context = {
                'animals' : animals,
                'animalList':animalList
            }
    return render(request, 'index.html', context)


def breed(request):
    animal = request.GET.get('animal')
    breeds = Breed.objects.filter(name=animal)
    context = {'breeds': breeds}
    return render(request, 'partials/breed.html', context)


@csrf_exempt
def addAnimal(request):
    animalId = request.POST.get('animal')
    breedId = request.POST.get('breed')
    animal = Animal.objects.get(id=animalId)
    breed = Breed.objects.get(id=breedId)
    obj = AnimalData(animalname=animal.name,breedname=breed.breedName)
    obj.save()
    animalList = AnimalData.objects.all()
    context = {'animalList':animalList}
    return render(request, 'partials/animalList.html', context)



@csrf_exempt
def deleteAnimal(request,pk):
    animal = AnimalData.objects.get(id=pk)
    animal.delete()
    animalList = AnimalData.objects.all()
    context = {'animalList':animalList}
    return render(request, 'partials/animalList.html', context)



