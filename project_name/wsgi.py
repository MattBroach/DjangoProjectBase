"""
WSGI config for floodgaming project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from {{project_name | lower}} import settings


os.environ.setdefault("DJANGO_LOCATION","production")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{project_name | lower}}.settings")


application = get_wsgi_application()

