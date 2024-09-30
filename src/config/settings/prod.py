from .base import *
from decouple import config

DEBUG = False

USE_HTTPS = config('USE_HTTPS', default='0', cast=bool)

if USE_HTTPS:
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')