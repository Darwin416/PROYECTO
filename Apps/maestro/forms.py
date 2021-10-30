from django import forms
from .models import Maestro

class MaestrosForm(forms.ModelForm):
     class Meta:
        model = Maestro
        fields = '__all__'