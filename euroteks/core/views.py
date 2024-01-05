from django.shortcuts import render


def page_not_found(request, exception):
    """
    Представление для отображения
    страницы с кодом ошибки 404.
    """

    template = 'core/404.html'
    return render(request, template, {'path': request.path}, status=404)
