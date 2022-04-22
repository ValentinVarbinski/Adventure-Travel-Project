from django import forms

from adventure_travel_final_project.at_experiences.models import AdventureTravelExperience


class AdventureTravelExperienceBookForm(forms.ModelForm):
    class Meta:
        model = AdventureTravelExperience
        fields = '__all__'
