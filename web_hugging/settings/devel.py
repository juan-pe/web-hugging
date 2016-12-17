# -*- coding: utf-8 -*-
from .base import *

DEBUG = True
ALLOWED_HOSTS = []

# filer
FILER_ENABLE_PERMISSIONS = True

# easy_thumbnails
THUMBNAIL_HIGH_RESOLUTION = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': bd_config['name'],
        'USER': bd_config['user'],
        'PASSWORD': bd_config['password'],
        'HOST': bd_config['host'],
        'PORT': bd_config['port'],
    }
}


THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(levelname)s [%(name)s %(filename)s:%(funcName)s:%(lineno)d] %(message)s'
        },
    },
    'handlers': {
        'debug': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        # 'django': {
        #     'handlers': ['debug'],
        #     'level': 'DEBUG',
        #     'propagate': True,
        # },
        'common': {
            'handlers': ['debug'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'cms': {
            'handlers': ['debug'],
            'level': 'DEBUG',
            'propagate': True,
        }
    },
}
