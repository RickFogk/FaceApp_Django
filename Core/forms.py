from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'age', 'gender', 'location', 'primary_disease', 'primary_concern', 'symptom_duration', 'question', 'emotional_state', 'consent']
