# -*- coding: utf-8 -*-
import json

from django.utils.translation import gettext_lazy as _

from .base import *

DEBUG = False
ALLOWED_HOSTS = ['bowie',
                 '178.62.193.36',
                 'www.huggingnepal.org',
                 'huggingnepal.org',
                 'test.huggingnepal.org']

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
    # 'djangocms_video',
    'djangocms_column',
    'djangocms_link',
    'reversion',
    'aldryn_bootstrap3',

    # personal
    'common',
]

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

# djago-cms templates
CMS_TEMPLATES = (
    ('common/template_inicio.html', _('Inicio')),
    ('common/template_proyectos.html', _('Proyectos')),
    ('common/template_lista_proyectos.html', _('Lista proyectos')),
    ('common/template_colabora.html', _('Colabora')),
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
