from django import forms
from django.contrib.auth import forms as auth_forms
from adventure_travel_final_project.at_profiles.models import AdventureTravelProfile
from adventure_travel_final_project.common.mixins import RemoveLabelFormMixin, BootstrapFormMixin


class UserProfileForm(BootstrapFormMixin, RemoveLabelFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self._init_bootstrap()

    class Meta:
        model = AdventureTravelProfile
        exclude = ('user',)

        widgets = {
            'first_name': forms.TextInput(
                attrs={'placeholder': 'First name'}
            ),
            'last_name': forms.TextInput(
                attrs={'placeholder': 'Last name'}
            ),

            'description': forms.TextInput(
                attrs={'placeholder': 'Describe yourself'}
            ),
            'facebook_account': forms.TextInput(
                attrs={'placeholder': 'Facebook'}
            ),
            'instagram_account': forms.TextInput(
                attrs={'placeholder': 'Instagram'}
            ),
            'twitter_account': forms.TextInput(
                attrs={'placeholder': 'Twitter'}
            ),
        }


class ChangePasswordForm(BootstrapFormMixin, RemoveLabelFormMixin, auth_forms.PasswordChangeForm):
    PASSWORD_MAX_LENGTH = 20

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self._init_bootstrap()

    old_password = forms.CharField(
        max_length=PASSWORD_MAX_LENGTH,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Enter your current password'}
        )
    )
    new_password1 = forms.CharField(
        max_length=PASSWORD_MAX_LENGTH,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Enter your new password'}
        )
    )
    new_password2 = forms.CharField(
        max_length=PASSWORD_MAX_LENGTH,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Confirm password'}
        )
    )

    class Meta:
        fields = '__all__'
