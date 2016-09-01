# -*- coding: utf-8 -*-
import json

from .base import *

DEBUG = False
ALLOWED_HOSTS = ['bowie',
                 '178.62.193.36',
                 'www.huggingnepal.org',
                 'huggingnepal.org',
                 'test.huggingnepal.org']

# filer
FILER_ENABLE_PERMISSIONS = True

# easy_thumbnails
THUMBNAIL_HIGH_RESOLUTION = True


THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    # 'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

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
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(BASE_DIR, 'logs/debug.log'),
        },
        'hugging': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(BASE_DIR, 'logs/hugging.log'),
        }
    },
    'loggers': {
        'django': {
            'handlers': ['debug'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'common': {
            'handlers': ['hugging'],
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
