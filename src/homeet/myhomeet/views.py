from django.shortcuts import render
from .models import HomeetUser
from .forms import HomeetUserCreationForm


def first_register(request):
    if request.method == 'POST':
        form = HomeetUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = HomeetUserCreationForm()
    return render(request, 'myhomeet/index1.html', {'title': 'О себе', 'form': form})


def second_register(request):
    print(request.method, request)
    if request.method == 'POST':
        print(request.method, request)
        form = HomeetUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = HomeetUserCreationForm()
    return render(request, 'myhomeet/index2.html', {'title': 'Образование', 'form': form})