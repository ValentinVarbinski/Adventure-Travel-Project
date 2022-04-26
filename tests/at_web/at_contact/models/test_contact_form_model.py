from django.core.exceptions import ValidationError

from tests.test_cases import AdventureTravelTestCases


class ContactFormModelTests(AdventureTravelTestCases):
    def test_contact_form_model_email_contain_non_english_letters__expect_exception(self):
        self.contact_form.email = 'вальо@aбв.бг'

        with self.assertRaises(ValidationError) as context:
            self.contact_form.full_clean()
            self.contact_form.save()

        self.assertIsNotNone(context.exception)

    def test_contact_form_model_subject_contain_non_english_letters__expect_exception(self):
        self.contact_form.subject = 'my събджект'

        with self.assertRaises(ValidationError) as context:
            self.contact_form.full_clean()
            self.contact_form.save()

        self.assertIsNotNone(context.exception)

    def test_contact_form_model_message_contain_non_english_letters__expect_exception(self):
        self.contact_form.message = 'моето съобщение'

        with self.assertRaises(ValidationError) as context:
            self.contact_form.full_clean()
            self.contact_form.save()

        self.assertIsNotNone(context.exception)
