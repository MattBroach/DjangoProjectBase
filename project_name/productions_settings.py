import os

from .base_settings import *

# Dev Environment specific settings
DEBUG = False 
ALLOWED_HOSTS = ['*']

#Staticfiles settings
STATIC_ROOT = os.path.join(BASE_DIR,'static')
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

# Development URLs
ROOT_URLCONF = '{{project_name | lower}}.production_urls'
