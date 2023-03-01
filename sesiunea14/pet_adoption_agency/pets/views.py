from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Pet


# Create your views here.


def index(request):
    return HttpResponse('Hello World! Here is the pets index')


def pets(request):
    pets_list = Pet.objects.all()
    return render(request, 'all_pets.html', {'pets': pets_list})


def pet_details(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)
    return render(request, 'pet_details.html', {'pet': pet})


def pet_add(request):
    pet_data = request.POST.dict()
    try:
        pet = Pet(
            name=pet_data['name'],
            location=pet_data['location'],
            gender=pet_data['gender'],
            species=pet_data['species']
        )
        pet.save()
    except (KeyError):
        return render(request, 'error.html', {'error_message': 'Error! Invalid pet details!'})
    return HttpResponseRedirect(reverse('pets:all_pets'))
