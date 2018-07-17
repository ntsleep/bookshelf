from django import template

register = template.Library()


@register.filter()
def get_book_action_status(value, action):
    return "on" if value.shelf_set.filter(action=action) else "off"
