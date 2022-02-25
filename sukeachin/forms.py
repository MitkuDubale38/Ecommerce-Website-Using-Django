from django import forms
from .models import Review




class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('name', 'email','review_body')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'id': 'email'}),
            'review_body': forms.Textarea(attrs={'class': 'form-control','id': 'review_body'}),

        }