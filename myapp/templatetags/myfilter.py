from django import template
# filter ko register karne ke liye
register = template.Library()


@register.filter(name='remove_special')
def remove_chars(value, arg):
    for character in arg:
        # jo [] laga han jab hum kisi ka resume dekhte han usse nahi dekhne ke liye we write this
        value = value.replace(character, "")
    return value
