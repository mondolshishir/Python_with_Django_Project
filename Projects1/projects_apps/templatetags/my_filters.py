from django import template
from django.contrib.auth.models import Group

register = template.Library()


def my_filter(value):
    return value + " This is a string from custom filter "


register.filter('custom_filter', my_filter)
