"""
Django settings for floodgaming project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!

#Use Environment Variable DJANGO_LOCATION to determine location:
#options are: local, staging, and production
DJANGO_LOCATION = os.environ['DJANGO_LOCATION']
 
from {{project_name | lower}}.secret_keys import DJANGO_KEY
SECRET_KEY = DJANGO_KEY

# SECURITY WARNING: don't run with debug turned on in production!
# SECURITY WARNING: don't run with debug turned on in production!
if DJANGO_LOCATION == 'local':
    ALLOWED_HOSTS = []

else:
    ALLOWED_HOSTS = []


if DJANGO_LOCATION == 'local':
    DEBUG = True
else:
    DEBUG = False


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
)

# django-debug-toolbar settings
if DEBUG:
    INSTALLED_APPS += ('debug_toolbar',)

    INTERNAL_IPS = ('::ffff:10.0.2.2',)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',

)

ROOT_URLCONF = '{{project_name | lower}}.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = '{{project_name | lower}}.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': '{{project_name | lower}}_db',
            'USER': 'postgres',
            'PASSWORD': 'password',
            'HOST': 'localhost',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'


#Set staticfiles for development
if DJANGO_LOCATION == 'local':
    STATIC_ROOT = '/vagrant/static/'
    MEDIA_ROOT = '/vagrant/media/'
else:
    STATIC_ROOT = '/{{project_name}}/static/'
    MEDIA_ROOT = '/{{project_name}}/media/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'extra_static'),
)


# Debug toolbar settings
DEBUG_TOOLBAR_PATCH_SETTINGS = False

