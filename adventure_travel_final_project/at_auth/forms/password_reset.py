from django import forms
from django.contrib.auth import forms as auth_forms

from adventure_travel_final_project.common.validators import validate_bot_catcher


class UserPasswordResetForm(auth_forms.PasswordResetForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'Enter your email'}
        )
    )

    bot_catcher = forms.CharField(
        widget=forms.HiddenInput,
        required=False,
    )

    def clean_bot_catcher(self):
        validate_bot_catcher(self.cleaned_data['bot_catcher'])


class UserSetNewPasswordForm(auth_forms.SetPasswordForm):
    PASSWORD_MAX_LENGTH = 20

    new_password1 = forms.CharField(
        max_length=PASSWORD_MAX_LENGTH,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Enter your new password'}
        )
    )

    new_password2 = forms.CharField(
        max_length=PASSWORD_MAX_LENGTH,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Confirm your new password'}
        )
    )

    bot_catcher = forms.CharField(
        widget=forms.HiddenInput,
        required=False,
    )

    def clean_bot_catcher(self):
        validate_bot_catcher(self.cleaned_data['bot_catcher'])