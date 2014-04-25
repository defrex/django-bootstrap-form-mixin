
from django import forms
from django.template.loader import render_to_string


class BootstrapForm(object):
    form_template = 'bootstrap_form/form.html'
    field_template = 'bootstrap_form/field.html'

    def as_bootstrap(self):
        for name, field in self.fields.iteritems():
            if not 'class' in field.widget.attrs:
                field.widget.attrs['class'] = ''
            if not isinstance(field.widget, forms.RadioSelect):
                field.widget.attrs['class'] += ' form-control'
            if 'group_class' in field.widget.attrs:
                field.widget.group_class = field.widget.attrs.pop('group_class')

        return render_to_string(self.form_template, {
            'form': self,
            'field_template': self.field_template,
        })
