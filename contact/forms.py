from django import forms

class ContactForm(forms.Form):
    choices = [(1, 'Teklif'), (2, 'Irad')]
    name = forms.CharField(max_length=30, min_length=3, widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Username'
    }))
    email = forms.EmailField(max_length=50,min_length=13, widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'Email'
    }))
    subject = forms.ChoiceField(choices=choices, widget=forms.Select(attrs={
        'class':'form-control',
        'placeholder':'Subject'
    }))
    messages = forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control',
        'placeholder':'Messages'
    }))