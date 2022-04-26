from django.test import TestCase

from adventure_travel_final_project.at_auth.forms.password_reset import UserSetNewPasswordForm


class UserSetNewPasswordFormTests(TestCase):
    # TEST FORM LABELS
    def test_set_new_password_form_password1_label__expect_empty_label(self):
        expected_label = ''
        form = UserSetNewPasswordForm(user='valio')
        self.assertEqual(expected_label, form['new_password1'].label)

    def test_set_new_password_form_password2_label__expect_empty_label(self):
        expected_label = ''
        form = UserSetNewPasswordForm(user='valio')
        self.assertEqual(expected_label, form['new_password2'].label)

    # TEST FORM CLASS FIELDS
    def test_set_new_password_form_password_class__expect_form_control_class(self):
        expected_class = 'form-control'
        form = UserSetNewPasswordForm(user='valio')
        self.assertEqual(expected_class, form.fields['new_password1'].widget.attrs['class'])

    def test_set_new_password_form_confirm_password_class__expect_form_control_class(self):
        expected_class = 'form-control'
        form = UserSetNewPasswordForm(user='valio')
        self.assertEqual(expected_class, form.fields['new_password2'].widget.attrs['class'])

    # TEST FORM PLACEHOLDERS
    def test_set_new_password_form_password_placeholder__expect_correct_placeholder(self):
        expected_placeholder = 'Enter your new password'
        form = UserSetNewPasswordForm(user='valio')
        self.assertEqual(expected_placeholder, form.fields['new_password1'].widget.attrs['placeholder'])

    def test_set_new_password_form_confirm_password_placeholder__expect_correct_placeholder(self):
        expected_placeholder = 'Enter your new password'
        form = UserSetNewPasswordForm(user='valio')
        self.assertEqual(expected_placeholder, form.fields['new_password1'].widget.attrs['placeholder'])
