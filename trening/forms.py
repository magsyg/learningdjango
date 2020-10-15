import json

from django import forms
from users.models import User
from trening import models as trening_models

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = trening_models.Workout
        fields = ['treningtype', 'distance', 'date']
        
    def _init_(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['distance'].widget.attrs.update({'placeholder': "eks 8.2 km"})

    