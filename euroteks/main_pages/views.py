from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect, render
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


def feedback(request):
    template = 'main_pages/feedback.html'
    form = FeedbackForm()
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            print('lol')
            form.save()
            return redirect('main_pages:success')
            # return HttpResponseRedirect('/success/')
    else:
        form = FeedbackForm()
    print('loooooooool')

    return render(request, template, {'form': form})

# class FeedbackView(CreateView):
#     """
#     Представление страницы с формой обратной связи.
#     """

#     form_class = FeedbackForm
#     template_name = 'main_pages/feedback.html'
#     success_url = '127.0.0.1:8000'
