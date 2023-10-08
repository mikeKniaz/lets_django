"""
WSGI config for lets_django project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from encrypted_secrets import load_secrets

if __name__ == "__main__":
    load_secrets()
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lets_django.settings')

application = get_wsgi_application()


