from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class Register(forms.ModelForm):
    confirmPassword = forms.CharField(max_length='30', widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'confirm password'
    }))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
    
        widgets = {
            'username':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'username'
            }),
            'first_name':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'first name'
            }),
            'last_name':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'last name'
            }),
            'email':forms.EmailInput(attrs={
                'class':'form-control',
                'placeholder':'Email'
            }),
            'password':forms.PasswordInput(attrs={
                'class':'form-control',
                'placeholder':'password'
            }),

        }
    def clean(self):
        confirmPassword = self.cleaned_data.get('confirmPassword')
        password = self.cleaned_data.get('password')

        if confirmPassword != password:
            raise forms.ValidationError('Confirm password and Password not equal')

        return super().clean()