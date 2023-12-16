from django import forms

from .models import Feedback


class FeedbackForm(forms.ModelForm):
    """
    Форма для обратной связи.
    """

    class Meta:
        model = Feedback
        fields = (
            'name',
            'surname',
            'text',
            'telephone',
            'email',
        )
        # labels = {'name': 'Имя', 'surname': 'Фамилия',
        #           'text': 'Сообщение', 'telephone': 'Телефон',
        #           'email': 'Email'}
        # help_texts = {
        #             'name': 'Имя', 'surname': 'Фамилия',
        #             'text': 'Сообщение', 'telephone': 'Телефон',
        #             'email': 'Email'}