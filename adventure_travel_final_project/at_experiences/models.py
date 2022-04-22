from django.core.validators import MinValueValidator
from django.db import models

from adventure_travel_final_project.at_auth.models import AdventureTravelUser
from adventure_travel_final_project.common.validators import validate_only_english_letters


class AdventureTravelExperience(models.Model):
    TITLE_MAX_LENGTH = 50
    DESCRIPTION_MAX_LENGTH = 200

    ADVENTURE = 'Adventure'
    HIKING = 'Hiking'
    SIGHTSEEING_TOUR = 'Sightseeing tour'
    WINTER_SPORT = 'Winter sport'

    CATEGORIES = [(x, x) for x in (ADVENTURE, HIKING, SIGHTSEEING_TOUR, WINTER_SPORT)]

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
        validators=(
            validate_only_english_letters,
        )
    )

    description = models.CharField(
        max_length=DESCRIPTION_MAX_LENGTH,
        validators=(
            validate_only_english_letters,
        )
    )

    experience_picture = models.ImageField(
        upload_to='experiences',
    )

    category = models.CharField(
        max_length=(max([len(x) for x, _ in CATEGORIES])),
        choices=CATEGORIES,
    )

    date = models.DateField()

    price = models.IntegerField(
        validators=(
            MinValueValidator(0),
        )
    )

    spots = models.IntegerField(
        validators=(
            MinValueValidator(0),
        )
    )

    class Meta:
        verbose_name = 'Experience'

    def __str__(self):
        return self.title


class AdventureTravelRegistration(models.Model):
    registration_date = models.DateTimeField(
        auto_now_add=True,
    )

    experience = models.ForeignKey(
        AdventureTravelExperience,
        on_delete=models.CASCADE
    )

    client = models.ForeignKey(
        AdventureTravelUser,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Registration log'
