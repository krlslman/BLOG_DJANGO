from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()  # required=True for default
    class Meta:
        model = User
        fields = ("username", "email")

    # we use this validation function on registration since email must be unique
    def clean_email(self):
        email = self.cleaned_data['email']  # get email from the registration form
        if User.objects.filter(email=email).exists():  # if same email is already at use
            raise forms.ValidationError(  # raise error
                "This email is already in use!"
            )
        return email