from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True



#whether the ecms app is on temporary mode or not
#a temporary mode means that the main features of the
#application are not available in production mode
ECMS_TMP=True

#whether the account app is temporarily not used
ACCOUNT_TMP=True

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

ALLOWED_HOSTS = ['127.0.0.1','localhost','0.0.0.0']

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': 'ustudynow_local_db',
#    }
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ustudynow_prod_db',
        'USER': 'ustudynowdb_admin',
        'PASSWORD': 'da13div08_pao',
        'HOST': 'localhost',
        'PORT': '',
    }
}
