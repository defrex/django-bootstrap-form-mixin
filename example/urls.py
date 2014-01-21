from django.conf.urls import patterns, url

from app.views import ExampleView

urlpatterns = patterns(
    '',
    url(r'^$', ExampleView.as_view()),
)
