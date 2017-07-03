"""
Django settings for ustdy project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
from .conf.prod import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&8fr)7&4&u(p1+^h1%=k597oq12$7bavxw7$822#24%c_^jedt'

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

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = [

     os.path.join(BASE_DIR,'static'),
     os.path.join(BASE_DIR,'media/courses'),
	 os.path.join(BASE_DIR,'media/library'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
]

STATIC_URL = '/static/'

#I need to have this like this otherwise I am getting an error when trying to upload
COURSES_URL = 'media/courses/'
LIBRARY_URL = 'media/library/'

#we have to change this from static to sth else because we have
#the same path in the STATICFILES_DIRS and throws when we run collectstatic
#collect static is where we collect the static files
STATIC_ROOT = os.path.join(BASE_DIR, "assets/")
COURSES_ROOT = os.path.join(BASE_DIR,"media/courses/")
LIBRARY_ROOT = os.path.join(BASE_DIR,"media/library/")

if DEBUG==True:
  print("Running under development mode")
