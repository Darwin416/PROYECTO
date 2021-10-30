from django import forms
from .models import Representante 

class RepresentantesForm(forms.ModelForm):
     class Meta:
        model = Representante
        fields = '__all__'