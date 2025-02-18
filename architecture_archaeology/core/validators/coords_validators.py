from django.core.exceptions import ValidationError

"""
Чтобы пользователь не вводил произвольные числа в поля с координатами - 
сделал такие валидаторы. Долгота не может быть больше 180 и меньше -180,
соотв. широта тоже должна быть в интервале - 90 и 90
"""

def validate_lat(value):
    if not -91 < value < 91:
        raise ValidationError(
            'Широта должна быть в интервале от -90 до 90 градусов',
            params={'lat': value}
        )


def validate_long(value):
    if not -181 < value < 181:
        raise ValidationError(
            'Долгота должна быть в интервале от -180 до 180 градусов'
        )
