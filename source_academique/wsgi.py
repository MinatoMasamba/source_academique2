"""
WSGI config for source_academique project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""


import os
import sys

# Chemin de votre projet
project_home = '/home/MasambaMinato/source_academique'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

os.environ['DJANGO_SETTINGS_MODULE'] = 'source_academique.settings'

import django
django.setup()

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
