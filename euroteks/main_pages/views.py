from django.shortcuts import redirect, render

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

    return render(request, template)


def feedback(request):
    template = 'main_pages/feedback.html'
    form = FeedbackForm()
    feedback_button_footer_off = True
    messages = {}
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        # print(form)
        if form.is_valid():
            form.save()
            return redirect('main_pages:success')
        # else:
            # dict_errs = form.errors
            # for key, _ in dict_errs.items():
            #     if key == 'captcha':
            #         messages[key] = '<ul class="errorlist"><li>КАПЧА.</li></ul>'
    else:
        form = FeedbackForm()

    return render(request, template, {
        'form': form,
        'feedback_button_footer_off': feedback_button_footer_off,
        'messages': messages})
