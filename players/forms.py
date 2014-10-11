from django import forms
from models import Player

class PlayerForm(forms.ModelForm):

    class Meta:
        model = Player
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'sport': forms.TextInput(attrs={'class': 'form-control'}),
            'league': forms.TextInput(attrs={'class': 'form-control'}),
            'team': forms.TextInput(attrs={'class': 'form-control'}),
        }
