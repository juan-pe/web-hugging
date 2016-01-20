import json
from .base import *

DEBUG = False
ALLOWED_HOSTS = ['bowie']

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
        'PORT': '5432',
    }
}

INSTALLED_APPS += [
    'common',
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/debug.log'),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}