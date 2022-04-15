import string

from django.core.exceptions import ValidationError


def validate_only_english_letters(value):
    for char in value.lower():
        if char.isalpha() and char not in string.ascii_lowercase:
            raise ValidationError('You are not allowed to use non-English letters')


def validate_bot_catcher(value):
    if value:
        raise ValidationError('BOT DETECTED')
