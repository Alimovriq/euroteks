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
