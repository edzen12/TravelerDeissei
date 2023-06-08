from django import forms

from apps.packages.models import Country


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = (
            'title',
        )
