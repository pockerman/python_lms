"""
WSGI config for ustdy project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

#whitenoise to servicing static files in production
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ustdy.settings")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
