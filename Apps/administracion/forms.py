from django import forms
from .models import Admin, Curso, Periodo, Salon, Seccion  

class AdminsForm(forms.ModelForm):
     class Meta:
        model = Admin
        fields = '__all__'

class CursoForm(forms.ModelForm):
     class Meta:
        model = Curso
        fields = '__all__'

class PeriodoForm(forms.ModelForm):
     class Meta:
        model = Periodo
        fields = '__all__'
        
class SeccionForm(forms.ModelForm):
     class Meta:
        model = Seccion
        fields = '__all__'

class SalonForm(forms.ModelForm):
     class Meta:
        model = Salon
        fields = '__all__'