from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin


class HomeetUserManager(BaseUserManager):
    def create_user(self, tg, password=None, **extra_fields):
        if not tg:
            raise ValueError('Tg address is required')
        user = self.model(tg=tg, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, tg, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(tg, password, **extra_fields)


class HomeetUser(AbstractBaseUser, PermissionsMixin):
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
        ('', 'Ступень образования'),
        ('bachelor', 'Бакалавриат'),
        ('magistracy', 'Магистратура'),
        ('postgraduate', 'Аспирантура'),
    ]

    choice_faculty = [
        ('', 'Факультет'),
        ('MIEM', 'МИЭМ'),
        ('FKN', 'ФКН'),
        ('VSHB', 'ВШБ'),
    ]

    choice_program = [
        ('', 'Образовательная программа'),
        ('IVT', 'ИВТ'),
        ('ITSS', 'ИТСС'),
        ('PM', 'ПМ'),
    ]

    endlevel = 'Complited'

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    name = models.CharField(max_length=100, verbose_name="Имя и фамилия")
    sex = models.CharField(max_length=1, choices=choice_sex, verbose_name="Пол")
    tg = models.CharField(max_length=50, unique=True, verbose_name="Ник в телеграме")
    number = models.CharField(max_length=12, verbose_name="Номер телефона")
    photo_ava = models.ImageField(upload_to="photos/", verbose_name="Аватар профиля")
    date_of_birth = models.DateField(verbose_name="Дата рождения")
    description = models.TextField(blank=False, verbose_name="О себе")
    who_are_you = models.CharField(max_length=1, choices=choice_role, verbose_name='Студент или сотрудник', null=True, blank=True)
    level = models.CharField(max_length=20, choices=choice_level + [(endlevel, 'Уже окончил')], null=True, blank=True, verbose_name='Курс')
    education = models.CharField(max_length=20, choices=choice_education, null=True, blank=True, verbose_name="Ступень образования")
    faculty = models.CharField(max_length=100, choices=choice_faculty, null=True, blank=True, verbose_name="Факультет")
    program = models.CharField(max_length=100, choices=choice_program, null=True, blank=True, verbose_name="Образовательная программа")
    work = models.CharField(max_length=150, verbose_name="Работа", default="Не работаю")
    year_start_work = models.DateField(null=True, blank=True, verbose_name="Начало работы")

    objects = HomeetUserManager()

    USERNAME_FIELD = 'tg'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
