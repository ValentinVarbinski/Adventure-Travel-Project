from django.core.validators import MinLengthValidator
from django.db import models

from adventure_travel_final_project.common.validators import validate_only_english_letters


class AdventureTravelContactForm(models.Model):
    EMAIL_MAX_LENGTH = 40
    EMAIL_MIN_LENGTH = 5

    SUBJECT_MAX_LENGTH = 40
    SUBJECT_MIN_LENGTH = 5

    MESSAGE_MAX_LENGTH = 400
    MESSAGE_MIN_LENGTH = 20

    email = models.EmailField(
        max_length=EMAIL_MAX_LENGTH,
        validators=(
            validate_only_english_letters,
            MinLengthValidator(EMAIL_MIN_LENGTH),
        )
    )

    subject = models.CharField(
        max_length=SUBJECT_MAX_LENGTH,
        validators=(
            validate_only_english_letters,
            MinLengthValidator(SUBJECT_MIN_LENGTH),
        )
    )

    message = models.TextField(
        max_length=MESSAGE_MAX_LENGTH,
        validators=(
            validate_only_english_letters,
            MinLengthValidator(MESSAGE_MIN_LENGTH),
        )
    )

    replied = models.BooleanField(
        default=False,
    )

    date_received = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        verbose_name = 'Contact Form'
