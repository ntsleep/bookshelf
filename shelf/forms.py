from django import forms

from shelf.models import ACTION_CHOICES


class MarkBookForm(forms.Form):
    book_id = forms.IntegerField()
    action = forms.ChoiceField(choices=ACTION_CHOICES.items())
    date = forms.DateField(required=False)
