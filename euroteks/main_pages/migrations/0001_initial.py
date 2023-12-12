# Generated by Django 3.2.16 on 2023-12-11 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=500, verbose_name='Текст')),
                ('telephone', models.IntegerField(verbose_name='Телефон')),
                ('email', models.EmailField(max_length=255, verbose_name='Электронная почта')),
                ('name', models.CharField(max_length=10, verbose_name='Имя')),
                ('surname', models.CharField(max_length=20, verbose_name='Фамилия')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
            ],
        ),
    ]
