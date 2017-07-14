from django import forms

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author  # model has a user field