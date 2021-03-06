import dj_database_url
from .settings import *

DATABASES = {
    'default': dj_database_url.config(),
}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

DEBUG = False
TEMPLATE_DEBUG = False