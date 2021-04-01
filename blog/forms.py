from blog.models import Email
from django import forms

class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['text']
        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {'text': ''}