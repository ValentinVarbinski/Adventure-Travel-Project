from adventure_travel_final_project.at_profiles.forms import UserProfileForm
from tests.test_cases import AdventureTravelTestCases


class UserProfileFormTests(AdventureTravelTestCases):
    # TEST FORM LABELS
    def test_user_profile_form_first_name_label__expect_empty_label(self):
        expected_label = ''
        form = UserProfileForm(self.profile)
        self.assertEqual(expected_label, form['first_name'].label)

    def test_user_profile_form_last_name_label__expect_empty_label(self):
        expected_label = ''
        form = UserProfileForm(self.profile)
        self.assertEqual(expected_label, form['last_name'].label)

    def test_user_profile_form_description_label__expect_empty_label(self):
        expected_label = ''
        form = UserProfileForm(self.profile)
        self.assertEqual(expected_label, form['description'].label)

    def test_user_profile_form_facebook_account_label__expect_empty_label(self):
        expected_label = ''
        form = UserProfileForm(self.profile)
        self.assertEqual(expected_label, form['facebook_account'].label)

    def test_user_profile_form_instagram_account_label__expect_empty_label(self):
        expected_label = ''
        form = UserProfileForm(self.profile)
        self.assertEqual(expected_label, form['instagram_account'].label)

    def test_user_profile_form_twitter_account_label__expect_empty_label(self):
        expected_label = ''
        form = UserProfileForm(self.profile)
        self.assertEqual(expected_label, form['twitter_account'].label)

    # TEST FORM PLACEHOLDERS

    def test_user_profile_form_first_name_placeholder__expect_correct_placeholder(self):
        expected_placeholder = 'First name'
        form = UserProfileForm()
        self.assertEqual(expected_placeholder, form.fields['first_name'].widget.attrs['placeholder'])

    def test_user_profile_form_last_name_placeholder__expect_correct_placeholder(self):
        expected_placeholder = 'Last name'
        form = UserProfileForm()
        self.assertEqual(expected_placeholder, form.fields['last_name'].widget.attrs['placeholder'])

    def test_user_profile_form_description_placeholder__expect_correct_placeholder(self):
        expected_placeholder = 'Describe yourself'
        form = UserProfileForm()
        self.assertEqual(expected_placeholder, form.fields['description'].widget.attrs['placeholder'])

    def test_user_profile_form_facebook_account_placeholder__expect_correct_placeholder(self):
        expected_placeholder = 'Facebook'
        form = UserProfileForm()
        self.assertEqual(expected_placeholder, form.fields['facebook_account'].widget.attrs['placeholder'])

    def test_user_profile_form_instagram_account_placeholder__expect_correct_placeholder(self):
        expected_placeholder = 'Instagram'
        form = UserProfileForm()
        self.assertEqual(expected_placeholder, form.fields['instagram_account'].widget.attrs['placeholder'])

    def test_user_profile_form_twitter_account_placeholder__expect_correct_placeholder(self):
        expected_placeholder = 'Twitter'
        form = UserProfileForm()
        self.assertEqual(expected_placeholder, form.fields['twitter_account'].widget.attrs['placeholder'])
