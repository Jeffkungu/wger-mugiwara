#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dj_database_url
import psycopg2
from wger.settings_global import *

# Use 'DEBUG = True' to get more details for server errors
DEBUG = True
TEMPLATES[0]['OPTIONS']['debug'] = True

ADMINS = (
    ('Your name', 'your_email@example.com'),
)
MANAGERS = ADMINS


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test_wger',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'w)x+u+qi%&5sdbe3-$%h+s)#44_&av5i5mr^3k-3ryuy=(%o#i'

# Your reCaptcha keys
RECAPTCHA_PUBLIC_KEY = ''
RECAPTCHA_PRIVATE_KEY = ''
NOCAPTCHA = True

# The site's URL (e.g. http://www.my-local-gym.com or http://localhost:8000)
# This is needed for uploaded files and images (exercise images, etc.) to be
# properly served.
SITE_URL = 'http://wger-mugiwara.herokuapp.com'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (os.path.join(BASE_DIR, "core", "static"),
                    os.path.join(BASE_DIR, "nutrition", "static"),
                    os.path.join(BASE_DIR, "weight", "static"),
                    os.path.join(BASE_DIR, "exercises", "static"),
                    os.path.join(BASE_DIR, "software", "static")
)
#  Add the Whitenoise to your Django application 
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
#STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    # added BowerFinder to list of static file finders
    'djangobower.finders.BowerFinder',

    # Django compressor
    'compressor.finders.CompressorFinder',
)
COMPRESS_OFFLINE = True

# Path to uploaded files
# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT = '/Users/faithngetich/.local/share/wger/media'
MEDIA_URL = '/media/'

# Allow all hosts to access the application. Change if used in production.
ALLOWED_HOSTS = ['wger-mugiwara.herokuapp.com']

# This might be a good idea if you setup memcached
#SESSION_ENGINE = "django.contrib.sessions.backends.cache"

DATABASE_URL = 'postgresql:///test_wger'
DATABASES = {'default': dj_database_url.config(default=DATABASE_URL)}
# Configure a real backend in production
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Sender address used for sent emails
WGER_SETTINGS['EMAIL_FROM'] = 'wger Workout Manager <wger@example.com>'

# Your twitter handle, if you have one for this instance.
#WGER_SETTINGS['TWITTER'] = ''
