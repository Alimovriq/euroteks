from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Feedback(models.Model):
    """
    Форма обратной связи.
    """

    name = models.CharField(
        'Имя', max_length=10,
        help_text='Введите имя')
    surname = models.CharField(
        'Фамилия',
        max_length=20,
        help_text='Введите фамилию')
    text = models.TextField(
        'Сообщение', max_length=500,
        help_text='Введите сообщение')
    # telephone = models.IntegerField(
    #     'Телефон',
    #     help_text='Введите номер телефона')
    telephone = PhoneNumberField(
        'Телефон',
        help_text='Введите номер телефона')
    email = models.EmailField(
        'Электронная почта',
        max_length=255,
        help_text='Введите email')
    pub_date = models.DateTimeField(
        'Дата',
        auto_now_add=True)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self) -> str:
        return f'Заявка №{self.pk}'
