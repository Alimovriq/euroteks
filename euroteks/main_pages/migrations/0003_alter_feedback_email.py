# Generated by Django 3.2.16 on 2023-12-16 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_pages', '0002_auto_20231212_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='email',
            field=models.EmailField(help_text='Введите email', max_length=255, verbose_name='Электронная почта'),
        ),
    ]
