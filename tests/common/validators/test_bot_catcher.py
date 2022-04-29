from django.core.exceptions import ValidationError
from django.test import TestCase

from adventure_travel_final_project.common.validators import validate_bot_catcher


class ValidateBotCatcherTests(TestCase):
    def test_when_bot_caught__expect_exception(self):
        value = 'caught bot'
        error_message = 'BOT DETECTED'

        with self.assertRaises(ValidationError) as context:
            validate_bot_catcher(value)

        self.assertEqual(error_message, context.exception.message)

    def test_when_field_empty__expect_running(self):
        value = ''
        validate_bot_catcher(value)

