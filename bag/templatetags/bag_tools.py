from django import template
# Some code here taken from boutique ado project

register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity
    