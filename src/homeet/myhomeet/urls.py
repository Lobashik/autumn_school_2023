from django.urls import path
from .views import *


urlpatterns = [
    path('', first_register, name='first'),
    path('education/', second_register, name='second'),
]