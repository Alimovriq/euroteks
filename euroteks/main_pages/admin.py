from django.contrib import admin

from .models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    """
    Админка для обратной связи.
    """

    list_display = (
        'pk',
        'text',
        'name',
        'surname',
        'telephone',
        'email',
        'pub_date',)
    list_filter = (
        'email',
        'name',
        'surname',)
    search_fields = (
        'email',
        'name',
        'surname')
    