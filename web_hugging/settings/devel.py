import json
from .base import *

DEBUG = True
ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

with open(os.getenv('WEB_CONFIG'), 'r') as f:
    bd_config = json.loads(f.read())


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': bd_config['name'],
        'USER': bd_config['user'],
        'PASSWORD': bd_config['password'],
        'HOST': 'localhost',
        'PORT': '5433',
    }
}

# Application definition

INSTALLED_APPS += [
    'common',
]
