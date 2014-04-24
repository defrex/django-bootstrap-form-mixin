### Django Bootstrap Form Mixin

`form.py`

    from django import forms

    from bootstrap_form.forms import BootstrapForm


    class ExampleForm(BootstrapForm, forms.Form):
        text = forms.CharField()


`my_template.html`

      <form>
        {{ form.as_bootstrap }}
        <button type="submit">Submit</button>
      </form>
