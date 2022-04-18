from django import forms

from adventure_travel_final_project.at_web.models import AdventureTravelContactForm
from adventure_travel_final_project.common.mixins import BootstrapFormMixin, RemoveLabelFormMixin
from adventure_travel_final_project.common.validators import validate_bot_catcher


class ContactForm(BootstrapFormMixin, RemoveLabelFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self._init_bootstrap()

    class Meta:
        model = AdventureTravelContactForm
        exclude = ('replied',)

        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Write your subject'}),
            'message': forms.Textarea(attrs={'placeholder': 'Write your message'}),
        }

    bot_catcher = forms.CharField(
        widget=forms.HiddenInput(),
        required=False,
    )

    def clean_bot_catcher(self):
        validate_bot_catcher(self.cleaned_data['bot_catcher'])

