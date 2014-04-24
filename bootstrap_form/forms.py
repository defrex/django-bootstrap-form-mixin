import types

from django.template.loader import render_to_string


class BootstrapForm(object):
    form_template = 'bootstrap_form/form.html'
    field_template = 'bootstrap_form/field.html'

    def as_bootstrap(self):
        for name, field in self.fields.iteritems():
            if not 'class' in field.widget.attrs:
                field.widget.attrs['class'] = ''
            field.widget.attrs['class'] += ' form-control'

        return render_to_string(self.form_template, {
            'form': self,
            'field_template': self.field_template,
        })
