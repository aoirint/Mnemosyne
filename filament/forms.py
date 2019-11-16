from django import forms
from filament.models import *

class FilamentForm(forms.Form):
    material = forms.ChoiceField(
        required=True,
        choices=FILAMENT_MATERIAL_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control',
            'form': 'filament_form',
        }),
    )
    amount = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'form': 'filament_form',
            'placeholder': 'g単位',
        }),
    )
    price = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'form': 'filament_form',
            'placeholder': '円単位',
        }),
    )
    shop = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'form': 'filament_form',
            'placeholder': 'Amazon',
        }),
    )
    url = forms.URLField(
        required=False,
        widget=forms.URLInput(attrs={
            'class': 'form-control',
            'form': 'filament_form',
            'placeholder': 'https://www.amazon.co.jp/dp/XXXXXXXXXX',
        }),
    )
    owner = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'form': 'filament_form',
            'placeholder': 'your name',
        }),
    )
    name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'form': 'filament_form',
            'placeholder': 'マイフィラメント',
        }),
    )
    image = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control',
            'form': 'filament_form',
        }),
    )
