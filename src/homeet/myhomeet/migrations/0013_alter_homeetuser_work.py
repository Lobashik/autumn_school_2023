# Generated by Django 4.2.7 on 2023-11-04 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myhomeet', '0012_alter_homeetuser_education_alter_homeetuser_faculty_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeetuser',
            name='work',
            field=models.CharField(default='Не работаю', max_length=150, verbose_name='Работа'),
        ),
    ]