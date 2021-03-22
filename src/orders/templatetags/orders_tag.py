from django import template

register = template.Library()


@register.filter
def check_order_status(status):
    return status in ['Завершен', 'Отменен', 'Отмена']