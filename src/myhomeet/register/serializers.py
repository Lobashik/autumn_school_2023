from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from datetime import datetime


USER = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    last_login = serializers.DateTimeField(default=datetime.now())
    token = serializers.CharField(max_length=255, read_only=True)

    def create(self, validated_data):
        user = USER.objects.create_user(**validated_data)
        raw_password = validated_data.get('password')
        user.set_password(raw_password)
        user.save()
        return user

    class Meta:
        model = USER
        exclude = ('user_permissions', 'groups', 'is_superuser', 
                   'is_staff', 'id')


class LoginSerializer(serializers.Serializer):
    tg = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        # В методе validate мы убеждаемся, что текущий экземпляр
        # LoginSerializer значение valid. В случае входа пользователя в систему
        # это означает подтверждение того, что присутствуют адрес электронной
        # почты и то, что эта комбинация соответствует одному из пользователей.
        tg = data.get('tg', None)
        password = data.get('password', None)

        # Вызвать исключение, если не предоставлена почта.
        if tg is None:
            raise serializers.ValidationError(
                'An tg is required to log in.'
            )

        # Вызвать исключение, если не предоставлен пароль.
        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        # Метод authenticate предоставляется Django и выполняет проверку, что
        # предоставленные почта и пароль соответствуют какому-то пользователю в
        # нашей базе данных. Мы передаем email как username, так как в модели
        # пользователя USERNAME_FIELD = email.
        user = authenticate(tg=tg, password=password)

        # Если пользователь с данными почтой/паролем не найден, то authenticate
        # вернет None. Возбудить исключение в таком случае.
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.'
            )

        # Django предоставляет флаг is_active для модели User. Его цель
        # сообщить, был ли пользователь деактивирован или заблокирован.
        # Проверить стоит, вызвать исключение в случае True.
        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

        # Метод validate должен возвращать словать проверенных данных. Это
        # данные, которые передются в т.ч. в методы create и update.
        return {
            'tg': user.tg,
            'name': user.name,
            'token': user.token
        }