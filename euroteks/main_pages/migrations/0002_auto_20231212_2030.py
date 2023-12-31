# Generated by Django 3.2.16 on 2023-12-12 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedback',
            options={'verbose_name': 'Заявка', 'verbose_name_plural': 'Заявки'},
        ),
        migrations.AlterField(
            model_name='feedback',
            name='email',
            field=models.EmailField(help_text='Введите емаил', max_length=255, verbose_name='Электронная почта'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='name',
            field=models.CharField(help_text='Введите имя', max_length=10, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='surname',
            field=models.CharField(help_text='Введите фамилию', max_length=20, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='telephone',
            field=models.IntegerField(help_text='Введите номер телефона', verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='text',
            field=models.TextField(help_text='Введите текст', max_length=500, verbose_name='Текст'),
        ),
    ]
