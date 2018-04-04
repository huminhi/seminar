from .base import *

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.01']

DATABASES['default']['HOST'] = os.environ.get('DJANGO_DATABASE_DEFAULT')
DATABASES['default']['USER'] = os.environ.get('DJANGO_DATABASE_USER')
DATABASES['default']['PASSWORD'] = os.environ.get('DJANGO_DATABASE_PASSWORD')
