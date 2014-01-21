
from django.views.generic.edit import FormView

from .forms import ExampleForm


class ExampleView(FormView):
    form_class = ExampleForm
    template_name = 'examples.html'
