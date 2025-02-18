from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def settings_value(name):
    """
    Функция для получения некоторых данных из настроек
    в темплейтах.
    """
    return getattr(settings, name, "")
