# -*- coding: utf-8 -*-
import json
from .base import *

DEBUG = False
ALLOWED_HOSTS = ['bowie',
                 '178.62.193.36',
                 'www.huggingnepal.org',
                 'huggingnepal.org',
                 'test.huggingnepal.org']

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
    # django-filer
    'easy_thumbnails',
    'filer',
    'mptt',

    # cmspugin-filer
    # 'cmsplugin_filer_file',
    # 'cmsplugin_filer_folder',
    # 'cmsplugin_filer_link',
    # 'cmsplugin_filer_image',
    # 'cmsplugin_filer_teaser',
    # 'cmsplugin_filer_video',

    # django-cms plugins
    'djangocms_inherit',
    'djangocms_file',
    'djangocms_picture',
    'djangocms_teaser',
    'djangocms_video',
    'djangocms_column',
    'djangocms_link',
    'reversion',
    'aldryn_bootstrap3',

    # personal
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
        'hugging': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/hugging.log'),
        }
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'common': {
            'handlers': ['hugging'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'cms': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        }
    },
}
