from django.db import models

from adventure_travel_final_project.common.validators import validate_only_english_letters


class AdventureTravelPostAuthor(models.Model):
    FIRST_NAME_MAX_LENGTH = 20
    LAST_NAME_MAX_LENGTH = 20

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            validate_only_english_letters,
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            validate_only_english_letters,
        )
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Author'


class AdventureTravelPost(models.Model):
    TITLE_MAX_LENGTH = 100
    CONTENT_MAX_LENGTH = 600

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
        unique=True,
        validators=(
            validate_only_english_letters,
        )
    )

    content = models.TextField(
        max_length=CONTENT_MAX_LENGTH,
        validators=(
            validate_only_english_letters,
        )
    )

    blog_picture = models.ImageField(
        upload_to='blog_pictures',

    )

    slug = models.SlugField(
        unique=True,
        validators=(
            validate_only_english_letters,
        )
    )

    created_on = models.DateField(
        auto_now_add=True,
    )

    author = models.ForeignKey(
        AdventureTravelPostAuthor,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Post'
