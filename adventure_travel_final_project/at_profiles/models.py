from django.core.validators import MinLengthValidator
from django.db import models

from adventure_travel_final_project.at_auth.models import AdventureTravelUser
from adventure_travel_final_project.common.validators import validate_only_english_letters


class AdventureTravelProfile(models.Model):
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 30

    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30

    FACEBOOK_ACCOUNT_MAX_LENGTH = 40
    INSTAGRAM_ACCOUNT_MAX_LENGTH = 40
    TWITTER_ACCOUNT_MAX_LENGTH = 40

    BULGARIA = 'Bulgaria'
    GREECE = 'Greece'
    ROMANIA = 'Romania'
    UNITED_KINGDOM = 'United Kingdom'

    COUNTRIES = [(x, x) for x in (BULGARIA, UNITED_KINGDOM, GREECE, ROMANIA)]

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        blank=True,
        validators=(
            validate_only_english_letters,
            MinLengthValidator(FIRST_NAME_MIN_LENGTH)
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MIN_LENGTH,
        blank=True,
        validators=(
            validate_only_english_letters,
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
        )
    )

    profile_picture = models.ImageField(
        upload_to='profiles',
        default='profiles/default_profile_pic.jpg'
    )

    description = models.TextField(
        null=True,
        blank=True,
        validators=(
            validate_only_english_letters,
        )
    )

    country = models.CharField(
        max_length=(max([len(x) for x, _ in COUNTRIES])),
        choices=COUNTRIES,
        blank=True,
    )

    facebook_account = models.CharField(
        max_length=FACEBOOK_ACCOUNT_MAX_LENGTH,
        blank=True,
        validators=(
            validate_only_english_letters,
        )
    )

    instagram_account = models.CharField(
        max_length=INSTAGRAM_ACCOUNT_MAX_LENGTH,
        blank=True,
        validators=(
            validate_only_english_letters,
        )
    )

    twitter_account = models.CharField(
        max_length=TWITTER_ACCOUNT_MAX_LENGTH,
        blank=True,
        validators=(
            validate_only_english_letters,
        )
    )

    user = models.OneToOneField(
        AdventureTravelUser,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'profile'
