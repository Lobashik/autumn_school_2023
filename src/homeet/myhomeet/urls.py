from django.urls import path
from .views import *


urlpatterns = [
    path('', first_register, name='first'),
    # path('works/', second_register(), name='second'),
]