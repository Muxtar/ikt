from typing import Any, Dict
from django import forms
from home.models import Subcribe

class SubcribeForm(forms.ModelForm):
    class Meta:
        model = Subcribe
        fields = ['email']
        widgets = {
            'email':forms.EmailInput(attrs={
                'class':'form-control',
                'placeholder':'Enter email address'
            })
        }
        
    # def clean(self) -> Dict[str, Any]:
    #     allowEmail = ['gmail.com', 'mail.ru']
    #     if self.instance.email not in allowEmail:
    #         raise forms.ValidationError('')
    #     return super().clean()