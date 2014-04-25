
from django import forms

from bootstrap_form.forms import BootstrapForm


class ExampleForm(BootstrapForm, forms.Form):
    text = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'extra-class',
        'group_class': 'extra-group-class',
    }))

    radio = forms.ChoiceField(
        choices=(('y', 'Yes'), ('n', 'No')),
        widget=forms.RadioSelect(),
    )
