"""
WSGI config for Community_Connect project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv

# Read .env file and set key/value inside it as environement variables
# see: http://github.com/theskumar/python-dotenv
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.development")

application = get_wsgi_application()
