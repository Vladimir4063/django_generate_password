from multiprocessing.dummy import active_children
from random import random
from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    generated_password = ''

    #obtengo dato del form, medianto la url
    lenght_form = int(request.GET.get('length'))
    activate_uppercase = request.GET.get('uppercase')
    activate_special = request.GET.get('special')
    activate_numbers = request.GET.get('numbers')

    if activate_uppercase:
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if activate_special:
        characters.extend(list('!"#$%&'))

    if activate_numbers:
        characters.extend(list('1234567890'))
        
    for i in range(lenght_form):
        generated_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': generated_password})