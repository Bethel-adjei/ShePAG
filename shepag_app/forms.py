# forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    
class SubscribeForm(forms.Form):
    email = forms.EmailField(label='Your email', max_length=100, widget=forms.EmailInput(attrs={'placeholder': 'Your email'}))
    
