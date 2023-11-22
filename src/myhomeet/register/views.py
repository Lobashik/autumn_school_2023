from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import logout, authenticate, login
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from . import serializers


USER = get_user_model()


class UserAPIView(APIView):
    serializer_class = serializers.UserSerializer
    def get(self, request):
        users = USER.objects.all()
        serializer = self.serializer_class(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            auth_user = authenticate(tg=user.tg, password=request.data.get('password'))
            if auth_user:
                login(request, auth_user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = USER.objects.all()

    @action(detail=False, methods=['post'])
    def register_and_login(self, request):
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            tg = serializer.validated_data['tg']
            password = serializer.validated_data['password']
            user = authenticate(tg=tg, password=password)
            if user:
                login(request, user)
                refresh = RefreshToken.for_user(user)
                return Response({
                    'message': 'Registration successful and user logged in.',
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }, status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserListView(ListAPIView):
    queryset = USER.objects.all()
    serializer_class = serializers.UserList
    permission_classes = (IsAuthenticated, )


def index(request):
    if request.user.is_authenticated:
        return render(request, 'register/index.html', {'login': 'Выйти из аккаунта', 'logname': 'logout'})
    else:
        return render(request, 'register/index.html', {'login': 'Войти в аккаунт', 'logname': 'login'})


def logout_user(request):
    logout(request)
    return redirect('register:register')


def login_user(request):
    if request.method == 'POST':
        tg = request.POST.get('tg')
        password = request.POST.get('password')
        user = authenticate(request, tg=tg, password=password)
        if user is not None:
            login(request, user)
            print(user)
            import pdb; pdb.set_trace()
            return redirect('register:register')
        return HttpResponse("Нет такого пользователя")
    return render(request, 'register/login.html', {'login': 'Назад', 'logname': 'go_back'})