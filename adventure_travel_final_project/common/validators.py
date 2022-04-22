import string

from django.core.exceptions import ValidationError


# DATABASE VALIDATORS
def validate_only_english_letters(value):
    for char in value.lower():
        if char.isalpha() and char not in string.ascii_lowercase:
            raise ValidationError('You are not allowed to use non-English letters')




# FORM VALIDATORS
def validate_bot_catcher(value):
    if value:
        raise ValidationError('BOT DETECTED')
