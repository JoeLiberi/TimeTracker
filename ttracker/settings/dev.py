from ttracker.settings.base import *


ALLOWED_HOSTS = ['*']
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"),
#     # os.path.join(PROJECT_ROOT, 'static'),
# ]

DEBUG=True

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATICFILES_LOCATION = '/static/'
MEDIAFILES_LOCATION = '/media/'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
