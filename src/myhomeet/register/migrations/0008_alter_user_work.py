# Generated by Django 4.2.7 on 2023-11-13 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0007_alter_user_work'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='work',
            field=models.CharField(default='Не работаю', max_length=150, verbose_name='Работа'),
        ),
    ]
