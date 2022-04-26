from tests.test_cases import AdventureTravelTestCases
from django.core.exceptions import ValidationError


class ExperienceModelTests(AdventureTravelTestCases):
    def test_experience_model_title_contain_non_english_letters__expect_exception(self):
        self.experience.title = 'Тур'

        with self.assertRaises(ValidationError) as context:
            self.contact_form.full_clean()
            self.contact_form.save()

        self.assertIsNotNone(context.exception)

    def test_experience_model_description_contain_non_english_letters__expect_exception(self):
        self.experience.description = 'one day тур'

        with self.assertRaises(ValidationError) as context:
            self.contact_form.full_clean()
            self.contact_form.save()

        self.assertIsNotNone(context.exception)