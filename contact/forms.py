from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ['name', 'lastname', 'gender', 'nacionality', 'profession', 'status', 'childs', 
                  'sport', 'music', 'food', 'drink', 'contact_type', 'subscription']