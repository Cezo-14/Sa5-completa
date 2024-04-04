from django import forms
from .models import Usuario  # Supondo que Usuario é o nome do seu modelo de usuário

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'data_nascimento', 'email', 'pais']





  

