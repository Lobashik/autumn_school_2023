from rest_framework import serializers
from django.contrib.auth import get_user_model
from datetime import datetime


USER = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    last_login = serializers.DateTimeField(default=datetime.now())

    def create(self, validated_data):
        raw_password = validated_data.get('password')
        user = USER.objects.create(
            tg=validated_data['tg'],
            name=validated_data.get('name'),
            sex=validated_data.get('sex'),
            number=validated_data.get('number'),
            photo_ava=validated_data.get('photo_ava'),
            date_of_birth=validated_data.get('date_of_birth'),
            description=validated_data.get('description'),
            who_are_you=validated_data.get('who_are_you'),
            level=validated_data.get('level'),
            education=validated_data.get('education'),
            faculty=validated_data.get('faculty'),
            program=validated_data.get('program'),
            work=validated_data.get('work'),
            year_start_work=validated_data.get('year_start_work'),
        )
        user.set_password(raw_password)
        user.save()
        return user

    class Meta:
        model = USER
        exclude = ('user_permissions', 'groups', 'is_superuser', 
                   'is_staff', 'id')
