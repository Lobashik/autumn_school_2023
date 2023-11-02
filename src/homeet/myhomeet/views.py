from django.shortcuts import render


def first_register(request):
    return render(request, 'myhomeet/index.html')