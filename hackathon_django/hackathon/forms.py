from django import forms


class SearchForm(forms.Form):
    class Meta:
        fields:('entry')