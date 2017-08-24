from django import forms

class NameForm(forms.Form):
    about=forms.ChoiceField(choices='about',widget=forms.RadioSelect())
