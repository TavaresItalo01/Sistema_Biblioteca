# usuarios/forms.py
from allauth.socialaccount.forms import SignupForm
from django import forms

class CustomSocialSignupForm(SignupForm):
    cpf = forms.CharField(
        max_length=11,
        required=True,
        label="CPF",
        widget=forms.TextInput(attrs={'placeholder': 'Digite seu CPF'})
    )

    def save(self, request):
        user = super(CustomSocialSignupForm, self).save(request)
        user.cpf = self.cleaned_data['cpf']
        user.save()
        return user
