from django import forms

from .models import ReviewBlog


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewBlog
        fields = (
            'name',
            'email',
            'message'
        )
