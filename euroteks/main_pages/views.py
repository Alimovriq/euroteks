from django.shortcuts import render
from django.views.generic.edit import CreateView

from .forms import FeedbackForm


def index(request):
    """
    Представление главной страницы.
    """

    template = 'main_pages/index.html'

    return render(request, template)


def about(request):
    """
    Представление страницы описания компании.
    """

    template = 'main_pages/about.html'

    return render(request, template)


def requisites(request):
    """
    Представление страницы с реквизитами компании.
    """

    template = 'main_pages/requisites.html'

    return render(request, template)


def success(request):
    """
    Представление страницы с сообщением
    об успешной отправке формы обратной
    связи.
    """

    template = 'main_pages/success.html'

    return render(request, template)


class FeedbackView(CreateView):
    """
    Представление страницы с формой обратной связи.
    """

    form_class = FeedbackForm
    template_name = 'main_pages/feedback.html'
    success_url = '/success/'
