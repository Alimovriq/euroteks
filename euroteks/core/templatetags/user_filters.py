from django import template

register = template.Library()


@register.filter
def addclass(field, css):
    if field.name != 'captcha':
        return field.as_widget(attrs={'class': css})
