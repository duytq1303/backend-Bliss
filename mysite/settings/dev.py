from __future__ import absolute_import, unicode_literals

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'neq2xgnx#-*6ku(k22^-+q(g(0a$a8y#hvsyxn5k^#u+zpg!en'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CORS_ORIGIN_ALLOW_ALL = True

try:
    from .local import *
except ImportError:
    pass
