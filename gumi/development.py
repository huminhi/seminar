from .base import *

DEBUG = True

DATABASES['default']['NAME'] = os.environ.get('DJANGO_DATABASE_NAME', 'seminar_development')
DATABASES['default']['HOST'] = os.environ.get('DJANGO_DATABASE_DEFAULT', '127.0.0.1')
DATABASES['default']['USER'] = os.environ.get('DJANGO_DATABASE_USER', 'root')
DATABASES['default']['PASSWORD'] = os.environ.get('DJANGO_DATABASE_PASSWORD', '123456')
