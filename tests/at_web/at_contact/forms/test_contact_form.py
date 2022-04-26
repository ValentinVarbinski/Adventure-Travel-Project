from django.test import TestCase

from adventure_travel_final_project.at_web.forms import ContactForm


class ContactFormTests(TestCase):
    # TEST FORM LABELS
    def test_contact_form_email_label__expect_empty_label(self):
        expected_label = ''
        form = ContactForm()
        self.assertEqual(expected_label, form['email'].label)

    def test_contact_subject_email_label__expect_empty_label(self):
        expected_label = ''
        form = ContactForm()
        self.assertEqual(expected_label, form['subject'].label)

    def test_contact_form_message_label__expect_empty_label(self):
        expected_label = ''
        form = ContactForm()
        self.assertEqual(expected_label, form['message'].label)

    # TEST FORM CLASS FIELDS
    def test_contact_form_email_class__expect_form_control_class(self):
        expected_class = 'form-control'
        form = ContactForm()
        self.assertEqual(expected_class, form.fields['email'].widget.attrs['class'])

    def test_contact_form_subject_class__expect_form_control_class(self):
        expected_class = 'form-control'
        form = ContactForm()
        self.assertEqual(expected_class, form.fields['subject'].widget.attrs['class'])

    def test_contact_form_message_class__expect_form_control_class(self):
        expected_class = 'form-control'
        form = ContactForm()
        self.assertEqual(expected_class, form.fields['message'].widget.attrs['class'])

    # TEST FORM PLACEHOLDERS

    def test_contact_form_email_placeholder__expect_correct_placeholder(self):
        expected_placeholder = 'Enter your email'
        form = ContactForm()
        self.assertEqual(expected_placeholder, form.fields['email'].widget.attrs['placeholder'])

    def test_contact_form_subject_placeholder__expect_correct_placeholder(self):
        expected_placeholder = 'Write your subject'
        form = ContactForm()
        self.assertEqual(expected_placeholder, form.fields['subject'].widget.attrs['placeholder'])

    def test_contact_form_message_placeholder__expect_correct_placeholder(self):
        expected_placeholder = 'Write your message'
        form = ContactForm()
        self.assertEqual(expected_placeholder, form.fields['message'].widget.attrs['placeholder'])