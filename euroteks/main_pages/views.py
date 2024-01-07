from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.mail import BadHeaderError, send_mail

from main_pages.models import Feedback

from euroteks.settings import DEFAULT_FROM_EMAIL

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


def ekviteks(request):
    """
    Представление страницы с описанием
    рубленного геотекстиля "ЭКВИТЕКС".
    """

    template = 'main_pages/ekviteks.html'

    return render(request, template)


def success(request):
    """
    Представление страницы с сообщением
    об успешной отправке формы обратной
    связи.
    """

    template = 'main_pages/success.html'
    if request.session.get('feedback_submitted'):
        del request.session['feedback_submitted']
        return render(request, template)
    return redirect('main_pages:index')


def feedback(request):
    """"
    Представление для формы обратеной связи.
    При POST запросе сохраняется экземпляр класса,
    далее отправляется электронное письмо, в обратном
    случае возвращается ошибка, при успешном отправлении
    пользователь перенаправляется на страницу успеха.
    """

    template = 'main_pages/feedback.html'
    form = FeedbackForm()
    feedback_button_footer_off = True
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            obj = Feedback.objects.all().order_by('-pub_date').first()
            subject = f'Заявка №{obj.pk} от {obj.pub_date}'
            message = f'Дата: {obj.pub_date}\nФИО: {obj.name} {obj.surname}\nСообщение: {obj.text}\nКонтакты: {obj.telephone} {obj.email}'
            try:
                send_mail(subject, message, DEFAULT_FROM_EMAIL, [DEFAULT_FROM_EMAIL])
            except BadHeaderError:
                return HttpResponse('Ошибка в отправке формы.')
            request.session['feedback_submitted'] = True
            return redirect('main_pages:success')
    else:
        form = FeedbackForm()

    return render(request, template, {
        'form': form,
        'feedback_button_footer_off': feedback_button_footer_off})
