from django.test import TestCase

from adventure_travel_final_project.at_auth.forms.auth import LoginForm


class RegisterFormTests(TestCase):
    # TEST FORM LABELS
    def test_login_form_username_label__expect_empty_label(self):
        expected_label = ''
        form = LoginForm()
        self.assertEqual(expected_label, form['username'].label)

    def test_login_form_password_label__expect_empty_label(self):
        expected_label = ''
        form = LoginForm()
        self.assertEqual(expected_label, form['password'].label)

    # TEST FORM CLASS FIELDS
    def test_login_form_username_class__expect_form_control_class(self):
        expected_class = 'form-control'
        form = LoginForm()
        self.assertEqual(expected_class, form.fields['username'].widget.attrs['class'])

    def test_login_form_password_class__expect_form_control_class(self):
        expected_class = 'form-control'
        form = LoginForm()
        self.assertEqual(expected_class, form.fields['password'].widget.attrs['class'])

    # TEST FORM PLACEHOLDERS
    def test_login_form_username_placeholder__expect_correct_placeholder(self):
        expected_placeholder = 'Enter your username'
        form = LoginForm()
        self.assertEqual(expected_placeholder, form.fields['username'].widget.attrs['placeholder'])

    def test_login_form_password_placeholder__expect_correct_placeholder(self):
        expected_placeholder = 'Enter your password'
        form = LoginForm()
        self.assertEqual(expected_placeholder, form.fields['password'].widget.attrs['placeholder'])
