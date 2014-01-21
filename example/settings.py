
DEBUG = True
SECRET_KEY = 's2cret'
ROOT_URLCONF = 'urls'
STATIC_URL = '/static/'

INSTALLED_APPS = (
    'django.contrib.staticfiles',
    'bootstrap_form',
    'app',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}
