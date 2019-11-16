from django import forms
from filament.models import *
from print3d.models import *

class Print3dForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        filament_choices = []
        for filament in Filament.objects.all():
            value = filament.id
            display = '%d. %s' % (filament.id, filament.name)

            filament_choices.append((value, display))

        self.fields['filament'].choices = filament_choices

    filament = forms.ChoiceField(
        required=True,
        choices=[],
        widget=forms.Select(attrs={
            'class': 'form-control',
            'form': 'print3d_form',
        }),
    )
    amount = forms.FloatField(
        required=True,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'form': 'print3d_form',
            'placeholder': 'g単位',
        }),
    )
    user = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'form': 'print3d_form',
            'placeholder': 'your name',
        }),
    )
    memo = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'form': 'print3d_form',
            'placeholder': 'memo',
        }),
    )
    image = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control',
            'form': 'print3d_form',
        }),
    )
