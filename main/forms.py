from django import forms
from .models import Tour
from django.forms import ModelForm, TextInput, Textarea, NumberInput, Select, FileInput


class TourForm(ModelForm):
    class Meta:
        model = Tour
        fields = ['title', 'description', 'country', 'duration', 'price', 'tour_type', 'rating', 'image']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть назву туру'
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть опис туру'
            }),
            'country': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть країну або місце призначення'
            }),
            'duration': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть тривалість туру у днях'
            }),
            'price': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть ціну'
            }),
            'tour_type': Select(attrs={
                'class': 'form-control'
            }),
            'rating': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть рейтинг (0-5)'
            }),
            'image': FileInput(attrs={
                'class': 'form-control-file'
            }),
        }

