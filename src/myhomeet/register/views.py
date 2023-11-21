from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import logout, authenticate, login
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .serializers import *
from .renderers import *


USER = get_user_model()


# class UserAPIView(APIView):
#     permission_classes = (AllowAny,)
#     renderer_classes = (renderers.UserJSONRenderer,)
#     serializer_class = serializers.UserSerializer
#     def get(self, request):
#         users = USER.objects.all()
#         serializer = self.serializer_class(users, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             auth_user = authenticate(tg=user.tg, password=request.data.get('password'))
#             if auth_user:
#                 login(request, auth_user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegistrationAPIView(APIView):
    """
    Разрешить всем пользователям (аутентифицированным и нет) доступ к данному эндпоинту.
    """
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def post(self, request):
        user = request.data.get('user', {})

        # Паттерн создания сериализатора, валидации и сохранения - довольно
        # стандартный, и его можно часто увидеть в реальных проектах.
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


# class UserViewSet(ModelViewSet):
#     serializer_class = serializers.UserSerializer
#     queryset = USER.objects.all()


def index(request):
    if request.user.is_authenticated:
        return render(request, 'register/index.html', {'login': 'Выйти из аккаунта', 'logname': 'logout'})
    else:
        return render(request, 'register/index.html', {'login': 'Войти в аккаунт', 'logname': 'login'})


def logout_user(request):
    logout(request)
    return redirect('register:register')


# def login_user(request):
#     if request.method == 'POST':
#         tg = request.POST.get('tg')
#         password = request.POST.get('password')
#         user = authenticate(request, tg=tg, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('register:register')
#         else:
#             return HttpResponse("Нет такого пользователя")
#     else:
#         return render(request, 'register/login.html', {'login': 'Назад', 'logname': 'go_back'})
    

class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data.get('user', {})

        # Обратите внимание, что мы не вызываем метод save() сериализатора, как
        # делали это для регистрации. Дело в том, что в данном случае нам
        # нечего сохранять. Вместо этого, метод validate() делает все нужное.
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)