from django import forms

from books.models import Author


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author  # model has a user field
