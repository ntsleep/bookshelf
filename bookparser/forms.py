from django import forms

from books.models import Author


class SourceLinkForm(forms.Form):
    url = forms.CharField()


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'name_orig', 'surname', 'surname_orig', 'birth_date', 'biography']
