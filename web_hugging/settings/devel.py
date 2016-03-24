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

# filer
FILER_ENABLE_PERMISSIONS = True

# easy_thumbnails
THUMBNAIL_HIGH_RESOLUTION = True


THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

# djago-cms templates
CMS_TEMPLATES = (
    ('common/template_inicio.html', 'Inicio'),
    ('common/footer.html', 'Footer')
)

MIGRATION_MODULES = {
    # Add also the following modules if you're using these plugins:
    'djangocms_file': 'djangocms_file.migrations_django',
    # 'djangocms_flash': 'djangocms_flash.migrations_django',
    # 'djangocms_googlemap': 'djangocms_googlemap.migrations_django',
    # 'djangocms_link': 'djangocms_link.migrations_django',
    'djangocms_picture': 'djangocms_picture.migrations_django',
    'djangocms_snippet': 'djangocms_snippet.migrations_django',
    'djangocms_teaser': 'djangocms_teaser.migrations_django',
    'djangocms_video': 'djangocms_video.migrations_django',
    'djangocms_text_ckeditor': 'djangocms_text_ckeditor.migrations_django',
}
