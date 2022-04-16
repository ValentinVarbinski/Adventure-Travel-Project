from django import forms
from django.contrib.auth import forms as auth_forms

from adventure_travel_final_project.common.mixins import BootstrapFormMixin, RemoveLabelFormMixin
from adventure_travel_final_project.common.validators import validate_bot_catcher


class UserPasswordResetForm(BootstrapFormMixin, RemoveLabelFormMixin, auth_forms.PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self._init_bootstrap()

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


class UserSetNewPasswordForm(BootstrapFormMixin, RemoveLabelFormMixin, auth_forms.SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self._init_bootstrap()

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
