from django import forms


class SearchForm(forms.Form):
    class Meta:
        fields:('keyword','post_date','set_aside')