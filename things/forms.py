from django import forms
from .models import Thing

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']

    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 15}),
        max_length=120,
        required=False
    )

    quantity = forms.IntegerField(
        widget=forms.NumberInput(attrs={'min': 0, 'max': 50}),
        validators=[MinValueValidator(0), MaxValueValidator(50)]
    )
