from django.test import TestCase

from adventure_travel_final_project.at_auth.forms.password_reset import UserPasswordResetForm


class UserPasswordResetFormTests(TestCase):
    def test_user_password_reset_form_email_label__expect_empty_label(self):
        expected_label = ''
        form = UserPasswordResetForm()
        self.assertEqual(expected_label, form['email'].label)

    def test_user_password_reset_form_email_class__expect_form_control_class(self):
        expected_class = 'form-control'
        form = UserPasswordResetForm()
        self.assertEqual(expected_class, form.fields['email'].widget.attrs['class'])

    def test_user_password_reset_form_email_placeholder__expect_correct_placeholder(self):
        expected_placeholder = 'Enter your email'
        form = UserPasswordResetForm()
        self.assertEqual(expected_placeholder, form.fields['email'].widget.attrs['placeholder'])
