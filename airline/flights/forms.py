from django import forms
from .models import Flight, Review

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['origin', 'destination', 'duration']
        widgets = {
            'origin': forms.Select(attrs={'class': 'form-control'}),
            'destination': forms.Select(attrs={'class': 'form-control'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Duration in minutes'}),
        }

class ReviewForm(forms.ModelForm):
    flight = forms.ModelChoiceField(
        queryset=Flight.objects.all(),
        label="Select Flight"
    )
    class Meta:
        model = Review
        fields = ['flight','name', 'rating', 'comment']