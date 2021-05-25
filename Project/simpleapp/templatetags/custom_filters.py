from django import template

register = template.Library()


@register.filter(name='multiply')
def multiply(value, arg):
    # проверим, что value - это строка, а arg - это число
    if isinstance(value, str) and isinstance(arg, int):
        return str(value) * arg
    else:
        raise ValueError(f'Нельзя умножить {type(value)} на {type(arg)}')
