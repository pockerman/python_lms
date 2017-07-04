from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

#whether the ecms app is on temporary mode or not
#a temporary mode means that the main features of the
#application are not available in production mode
ECMS_TMP=True

#whether the account app is temporarily not used
ACCOUNT_TMP=True

#EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

#When DEBUG is False and a view raises an exception, all information
#will be sent by email to the people listed in the ADMINS setting. Make sure to
#replace the name/e-mail tuple above with your own information.
ADMINS = (('ustudynowdb_admin','ustudynowteam@gmail.com'),)

#Since DEBUG is False , Django will only allow the hosts
#included in this list to serve the application. This is a security measure.
ALLOWED_HOSTS = ['127.0.0.1','0.0.0.0','ustudynow.herokuapp.com', 'www.ustudynow.herokuapp.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        #'NAME': 'ustudynow_prod_db',
        #'USER': 'ustudynowdb_admin',
        #'PASSWORD': 'da13div08_pao',
        #'HOST': 'localhost',
        #'PORT': '',
    }
}

import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env) #  dj_database_url.config()
