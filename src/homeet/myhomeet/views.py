from django.shortcuts import render, redirect
from .models import HomeetUser
from .forms import HomeetUserCreationForm
from django.core.files.storage import default_storage
from datetime import date


def first_register(request):
    if request.method == 'POST':
        form = HomeetUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            if 'photo_ava' in request.FILES:
                uploaded_file = request.FILES['photo_ava']
                print(type(uploaded_file))
                file_name = default_storage.save(uploaded_file.name, uploaded_file)
                url = default_storage.url(file_name)
                print(data['photo_ava'])
                data['photo_ava'] = url[7:]
                data['date_of_birth'] = data['date_of_birth'].isoformat()
                print(data['photo_ava'])
            request.session['first_page_data'] = data
            return redirect('second')
    else:
        form = HomeetUserCreationForm()
    return render(request, 'myhomeet/index1.html', {'title': 'О себе', 'form': form})


def second_register(request):
    if request.method == 'POST':
        form = HomeetUserCreationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            first_page_data = request.session.get('first_page_data', {})
            first_page_data = dict(list(first_page_data.items())[:7])
            data = dict(list(data.items())[7:])
            all_data = {**first_page_data, **data}
            if all_data['endlevel'] is not True:
                del all_data['endlevel']
            else:
                all_data['level'] = 'Уже окончил'
                del all_data['endlevel']
            print(all_data, first_page_data)
            model = HomeetUser(**all_data)
            model.save()
    else:
        form = HomeetUserCreationForm()
    return render(request, 'myhomeet/index2.html', {'title': 'Образование', 'form': form})
