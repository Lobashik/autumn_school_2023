from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('name', 'sex', 'tg', 'number', 'photo_ava',
                  'date_of_birth', 'description', 'who_are_you',
                  'level', 'education', 'faculty', 'program',
                  'work', 'year_start_work')
