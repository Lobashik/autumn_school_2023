from django import forms
from .models import HomeetUser


class HomeetUserCreationForm(forms.ModelForm):
    choice_sex = [
        ('M', 'Парень'),
        ('F', 'Девушка'),
    ]

    choice_role = [
        ('E', 'Сотрудник'),
        ('S', 'Студент'),
    ]

    choice_level = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    ]

    choice_education = [
        ('bachelor', 'Бакалавриат'),
        ('magistracy', 'Магистратура'),
        ('postgraduate', 'Аспирантура'),
    ]

    choice_faculty = [
        ('MIEM', 'МИЭМ'),
        ('FKN', 'ФКН'),
        ('VSHB', 'ВШБ'),
    ]

    choice_program = [
        ('IVT', 'ИВТ'),
        ('ITSS', 'ИТСС'),
        ('PM', 'ПМ'),
    ]

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input_text'}))
    sex = forms.ChoiceField(choices=choice_sex, widget=forms.RadioSelect(attrs={'class': 'sex'}))
    tg = forms.CharField(widget=forms.TextInput(attrs={'class': 'input_text', 'placeholder': 'Ник в телеграме'}))
    number = forms.CharField(widget=forms.TextInput(attrs={'class': 'input_text', 'placeholder': 'Номер телефона'}))
    photo_ava = forms.ImageField(widget=forms.FileInput(attrs={'id': 'input_file', 'accept': '.png,.jpg,.jpeg', 'style': 'display: none'}))
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'class': 'data', 'placeholder': 'Дата рождения', 'type': 'date'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'input_text textarea'}))
    who_are_you = forms.ChoiceField(choices=choice_role, widget=forms.RadioSelect(attrs={'name': 'radio', 'class': 'radio-label'}))
    level = forms.ChoiceField(choices=choice_level, widget=forms.RadioSelect(choices=choice_level, attrs={'name': 'grade', 'style': 'display: none'}))
    endlevel = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'id': 'end', 'name': 'grade'}))
    education = forms.ChoiceField(choices=choice_education, widget=forms.Select(attrs={'class': 'select_level_education'}))
    faculty = forms.ChoiceField(choices=choice_faculty, widget=forms.Select(attrs={'class': 'select_level_education'}))
    program = forms.ChoiceField(choices=choice_program, widget=forms.Select(attrs={'class': 'select_level_education'}))
    work = forms.CharField(widget=forms.TextInput(attrs={'class': 'input_text page2_text', 'placeholder': 'Кем вы работаете?'}))
    year_start_work = forms.DateField(label="Год начала работы", widget=forms.DateInput(attrs={'class': 'data'}))

    class Meta:
        model = HomeetUser
        fields = (
            'name', 'sex', 'tg', 'number', 'photo_ava', 'date_of_birth',
            'description', 'who_are_you', 'level', 'endlevel', 'education',
            'faculty', 'program', 'work', 'year_start_work',
            )

