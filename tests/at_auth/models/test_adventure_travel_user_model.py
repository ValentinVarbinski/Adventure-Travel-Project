from django.core.exceptions import ValidationError

from tests.test_cases import AdventureTravelTestCases


class AdventureTravelUserModelTests(AdventureTravelTestCases):
    def test_user_model_username_contain_non_english_letters__expect_exception(self):
        self.user.username = 'Вальо'

        with self.assertRaises(ValidationError) as context:
            self.user.full_clean()
            self.user.save()

        self.assertIsNotNone(context.exception)

    def test_user_model_email_contain_non_english_letters__expect_exception(self):
        self.user.email = 'Вальо@абв.бг'

        with self.assertRaises(ValidationError) as context:
            self.user.full_clean()
            self.user.save()

        self.assertIsNotNone(context.exception)
