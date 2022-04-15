from django.db import models

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinLengthValidator
from django.db import models

from adventure_travel_final_project.common.managers import AdventureTravelManager
from adventure_travel_final_project.common.validators import validate_only_english_letters


class AdventureTravelUser(AbstractBaseUser, PermissionsMixin):
    USERNAME_MAX_LENGTH = 20
    USERNAME_MIN_LENGTH = 5

    EMAIL_MAX_LENGTH = 40
    EMAIL_MIN_LENGTH = 5

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        unique=True,
        validators=(
            validate_only_english_letters,
            MinLengthValidator(USERNAME_MIN_LENGTH),
        )
    )

    email = models.EmailField(
        max_length=EMAIL_MAX_LENGTH,
        unique=True,
        validators=(
            validate_only_english_letters,
            MinLengthValidator(EMAIL_MIN_LENGTH),
        )
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    is_verified = models.BooleanField(
        default=False,
    )

    is_active = models.BooleanField(
        default=True,
    )

    USERNAME_FIELD = 'username'

    objects = AdventureTravelManager()

    class Meta:
        verbose_name = 'User'



