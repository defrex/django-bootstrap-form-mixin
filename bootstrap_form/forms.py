
import types

from django.template.loader import render_to_string


class BootstrapForm(object):
    form_template = 'bootstrap_form/form.html'
    field_template = 'bootstrap_form/field.html'

    def as_bootstrap(self):
        if hasattr(self, 'field_order'):
            new_order = []
            for field in self.field_order:
                if field in self.fields.keyOrder:
                    new_order.append(field)
            self.fields.keyOrder = new_order

        for name, field in self.fields.iteritems():
            if not 'class' in field.widget.attrs:
                field.widget.attrs['class'] = ''
            field.widget.attrs['class'] += ' form-control'

        return render_to_string(self.form_template, {
            'form': self,
            'field_template': self.field_template,
        })

    def __iter__(self):
        for name in self.fields:
            if (
                hasattr(self, name) and
                isinstance(getattr(self, name), types.StringTypes)
            ):
                yield getattr(self, name)
            else:
                yield self[name]
