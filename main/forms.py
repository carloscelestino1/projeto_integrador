from django import forms
from . models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Foto_Form(forms.ModelForm):
    class Meta:
        model = Foto_Cadastrados
        fields = ['id_pessoa', 'foto']
        widgets = {
            'id_pessoa': forms.Select(attrs={'class': 'form-control'}),
        }


class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servios
        fields = '__all__'

class CadastroForm(forms.ModelForm):
    class Meta:
        model = Cadastrados
        fields = '__all__'
