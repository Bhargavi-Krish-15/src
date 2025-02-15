from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField()
    from_email = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)