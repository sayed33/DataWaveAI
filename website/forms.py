from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['full_name', 'email', 'phone', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control form-control-lg border-primary'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-lg border-primary'}),
            'phone': forms.TextInput(attrs={'class': 'form-control form-control-lg border-primary'}),
            'message': forms.Textarea(attrs={'class': 'form-control border-primary', 'rows': 5}),
        }
