from django import forms


class SearchForm(forms.Form):
    class Meta:
        fields:('title','post_date','set_aside')
   