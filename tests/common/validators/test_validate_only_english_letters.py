from django.core.exceptions import ValidationError
from django.test import TestCase

from adventure_travel_final_project.common.validators import validate_only_english_letters


class ValidateOnlyEnglishLettersTests(TestCase):
    def test_non_english_letters__expect_exception(self):
        value = 'тест'
        error_message = 'You are not allowed to use non-English letters'

        with self.assertRaises(ValidationError) as context:
            validate_only_english_letters(value)

        self.assertEquals(error_message, context.exception.message)

    def test_english_letters__expect_running(self):
        value = 'test'
        validate_only_english_letters(value)
