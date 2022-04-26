from django.test import TestCase

from adventure_travel_final_project.at_auth.forms.auth import RegisterForm


class LoginFormTests(TestCase):

    # TEST FORM LABELS
    def test_register_form_username_label__expect_empty_label(self):
        expected_label = ''
        form = RegisterForm()
        self.assertEqual(expected_label, form['username'].label)

    def test_register_form_email_label__expect_empty_label(self):
        expected_label = ''
        form = RegisterForm()
        self.assertEqual(expected_label, form['email'].label)

    def test_register_form_password_label__expect_empty_label(self):
        expected_label = ''
        form = RegisterForm()
        self.assertEqual(expected_label, form['password1'].label)

    def test_register_form_confirm_password_label__expect_empty_label(self):
        expected_label = ''
        form = RegisterForm()
        self.assertEqual(expected_label, form['password2'].label)

    # TEST FORM CLASS FIELDS
    def test_login_form_username_class__expect_form_control_class(self):
        expected_class = 'form-control'
        form = RegisterForm()
        self.assertEqual(expected_class, form.fields['username'].widget.attrs['class'])

    def test_login_form_email_class__expect_form_control_class(self):
        expected_class = 'form-control'
        form = RegisterForm()
        self.assertEqual(expected_class, form.fields['email'].widget.attrs['class'])

    def test_login_form_password_class__expect_form_control_class(self):
        expected_class = 'form-control'
        form = RegisterForm()
        self.assertEqual(expected_class, form.fields['password1'].widget.attrs['class'])

    def test_login_form_confirm_password_class__expect_form_control_class(self):
        expected_class = 'form-control'
        form = RegisterForm()
        self.assertEqual(expected_class, form.fields['password2'].widget.attrs['class'])

    # TEST FORM PLACEHOLDERS
    def test_login_form_username_placeholder__expect_correct_placeholder(self):
        expected_placeholder = 'Enter your username'
        form = RegisterForm()
        self.assertEqual(expected_placeholder, form.fields['username'].widget.attrs['placeholder'])

    def test_login_form_email_placeholder__expect_correct_placeholder(self):
        expected_placeholder = 'Enter your email'
        form = RegisterForm()
        self.assertEqual(expected_placeholder, form.fields['email'].widget.attrs['placeholder'])

    def test_login_form_password_placeholder__expect_correct_placeholder(self):
        expected_placeholder = 'Enter your password'
        form = RegisterForm()
        self.assertEqual(expected_placeholder, form.fields['password1'].widget.attrs['placeholder'])

    def test_login_form_confirm_password_placeholder__expect_correct_placeholder(self):
        expected_placeholder = 'Confirm your password'
        form = RegisterForm()
        self.assertEqual(expected_placeholder, form.fields['password2'].widget.attrs['placeholder'])
