from django.shortcuts import render, redirect
from .models import HomeetUser
from .forms import HomeetUserCreationForm


def first_register(request):
    if request.method == 'POST':
        form = HomeetUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('second')
    else:
        form = HomeetUserCreationForm()
    return render(request, 'myhomeet/index1.html', {'title': 'О себе', 'form': form})


def second_register(request):
    if request.method == 'POST':
        form = HomeetUserCreationForm(request.POST)
        if form.is_valid():
            print(1)
    else:
        form = HomeetUserCreationForm()
    return render(request, 'myhomeet/index2.html', {'title': 'Образование', 'form': form})
