
from django import forms

from bootstrap_form.forms import BootstrapForm


class ExampleForm(BootstrapForm, forms.Form):
    text = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'extra-class',
        'group_class': 'extra-group-class',
    }))
