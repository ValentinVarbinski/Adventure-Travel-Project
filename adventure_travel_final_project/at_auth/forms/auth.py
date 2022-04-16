from django.contrib.auth import forms as auth_forms
from django import forms

from adventure_travel_final_project.at_auth.models import AdventureTravelUser
from adventure_travel_final_project.common.mixins import BootstrapFormMixin, RemoveLabelFormMixin
from adventure_travel_final_project.common.validators import validate_bot_catcher


class RegisterForm(BootstrapFormMixin, RemoveLabelFormMixin, auth_forms.UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self._init_bootstrap()

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Enter your password'}
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Confirm your password'}
        )
    )

    bot_catcher = forms.CharField(
        widget=forms.HiddenInput(),
        required=False,
    )

    class Meta:
        model = AdventureTravelUser
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(
                attrs={'placeholder': 'Enter your username'}
            ),
            'email': forms.TextInput(
                attrs={'placeholder': 'Enter your email'}
            ),
        }

    def clean_bot_catcher(self):
        validate_bot_catcher(self.cleaned_data['bot_catcher'])


class LoginForm(BootstrapFormMixin, RemoveLabelFormMixin, auth_forms.AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self._init_bootstrap()

    USERNAME_MAX_LENGTH = 10
    PASSWORD_MAX_LENGTH = 20

    username = forms.CharField(
        max_length=USERNAME_MAX_LENGTH,
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter your username'}
        )
    )

    password = forms.CharField(
        max_length=PASSWORD_MAX_LENGTH,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Enter your password'}
        )
    )

    bot_catcher = forms.CharField(
        widget=forms.HiddenInput(),
        required=False,
    )

    def clean_bot_catcher(self):
        validate_bot_catcher(self.cleaned_data['bot_catcher'])
