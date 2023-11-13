from rest_framework import serializers
from django.contrib.auth import get_user_model


USER = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = USER
        fields = ('name', 'sex', 'tg', 'number', 'photo_ava',
                  'date_of_birth', 'description', 'who_are_you',
                  'level', 'education', 'faculty', 'program',
                  'work', 'year_start_work', 'password')
    
    def create(self, validated_data):
        raw_password = validated_data.get('password')
        user = USER.objects.create(
            tg=validated_data['tg']
        )
        user.set_password(raw_password)
        user.save()
        return user
