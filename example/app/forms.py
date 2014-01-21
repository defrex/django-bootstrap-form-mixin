
from django import forms

from bootstrap_form.forms import BootstrapForm


class ExampleForm(BootstrapForm, forms.Form):
    text = forms.CharField()
