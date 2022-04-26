from adventure_travel_final_project.at_profiles.forms import ChangePasswordForm
from tests.test_cases import AdventureTravelTestCases


class ChangePasswordFormTests(AdventureTravelTestCases):
    # TEST FORM LABELS
    def test_change_password_form_old_password_label__expect_empty_label(self):
        expected_label = ''
        form = ChangePasswordForm(self.password_change)
        self.assertEqual(expected_label, form['old_password'].label)

    def test_change_password_form_new_password_label__expect_empty_label(self):
        expected_label = ''
        form = ChangePasswordForm(self.password_change)
        self.assertEqual(expected_label, form['new_password1'].label)

    def test_change_password_form_confirm_new_password_label__expect_empty_label(self):
        expected_label = ''
        form = ChangePasswordForm(self.password_change)
        self.assertEqual(expected_label, form['new_password2'].label)

    # TEST FORM CLASS FIELDS

    def test_change_password_form_old_password_class__expect_form_control_class(self):
        expected_class = 'form-control'
        form = ChangePasswordForm(self.password_change)
        self.assertEqual(expected_class, form.fields['old_password'].widget.attrs['class'])

    def test_change_password_form_new_password_class__expect_form_control_class(self):
        expected_class = 'form-control'
        form = ChangePasswordForm(self.password_change)
        self.assertEqual(expected_class, form.fields['new_password1'].widget.attrs['class'])

    def test_change_password_form_confirm_new_password_class__expect_form_control_class(self):
        expected_class = 'form-control'
        form = ChangePasswordForm(self.password_change)
        self.assertEqual(expected_class, form.fields['new_password2'].widget.attrs['class'])

    # TEST FORM PLACEHOLDERS

    def test_change_password_form_old_password_placeholder__expect_correct_placeholder(self):
        expected_placeholder = 'Enter your current password'
        form = ChangePasswordForm(self.password_change)
        self.assertEqual(expected_placeholder, form.fields['old_password'].widget.attrs['placeholder'])

    def test_change_password_form_new_password_placeholder__expect_correct_placeholder(self):
        expected_placeholder = 'Enter your new password'
        form = ChangePasswordForm(self.password_change)
        self.assertEqual(expected_placeholder, form.fields['new_password1'].widget.attrs['placeholder'])

    def test_change_password_form_confirm_new_password_placeholder__expect_correct_placeholder(self):
        expected_placeholder = 'Confirm password'
        form = ChangePasswordForm(self.password_change)
        self.assertEqual(expected_placeholder, form.fields['new_password2'].widget.attrs['placeholder'])