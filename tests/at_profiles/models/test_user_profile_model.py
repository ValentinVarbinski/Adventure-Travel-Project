from django.core.exceptions import ValidationError

from tests.test_cases import AdventureTravelTestCases


class AdventureTravelProfileModelTests(AdventureTravelTestCases):
    def test_profile_model_first_name_contain_non_english_letters__expect_exception(self):
        self.profile.first_name = 'Валентин'

        with self.assertRaises(ValidationError) as context:
            self.contact_form.full_clean()
            self.contact_form.save()

        self.assertIsNotNone(context.exception)

    def test_profile_model_last_name_contain_non_english_letters__expect_exception(self):
        self.profile.last_name = 'Varбински'

        with self.assertRaises(ValidationError) as context:
            self.contact_form.full_clean()
            self.contact_form.save()

        self.assertIsNotNone(context.exception)

    def test_profile_model_description_contain_non_english_letters__expect_exception(self):
        self.profile.description = 'описание'

        with self.assertRaises(ValidationError) as context:
            self.contact_form.full_clean()
            self.contact_form.save()

        self.assertIsNotNone(context.exception)

    def test_profile_model_facebook_account_contain_non_english_letters__expect_exception(self):
        self.profile.facebook_account = 'фб'

        with self.assertRaises(ValidationError) as context:
            self.contact_form.full_clean()
            self.contact_form.save()

        self.assertIsNotNone(context.exception)

    def test_profile_model_twitter_account_contain_non_english_letters__expect_exception(self):
        self.profile.twitter_account = 'туит'

        with self.assertRaises(ValidationError) as context:
            self.contact_form.full_clean()
            self.contact_form.save()

        self.assertIsNotNone(context.exception)

    def test_profile_model_instagram_account_contain_non_english_letters__expect_exception(self):
        self.profile.instagram_account = 'instaграм'

        with self.assertRaises(ValidationError) as context:
            self.contact_form.full_clean()
            self.contact_form.save()

        self.assertIsNotNone(context.exception)

