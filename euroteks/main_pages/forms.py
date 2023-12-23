from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import Field
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox

from .models import Feedback


class FeedbackForm(forms.ModelForm):
    """
    Форма для обратной связи.
    """

    captcha = ReCaptchaField(label='Капча', widget=ReCaptchaV2Checkbox())
    success_url = 'main_pages:success'

    class Meta:
        model = Feedback
        fields = (
            'name',
            'surname',
            'text',
            'telephone',
            'email',
        )
        labels = {'name': 'Имя ', 'surname': 'Фамилия ',
                  'text': 'Сообщение ', 'telephone': 'Телефон ',
                  'email': 'Email '}
        help_texts = {'telephone': 'Введите номер телефона. Формат: +79681231231'}

    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Field(
            'name', css_class='asteriskField')
