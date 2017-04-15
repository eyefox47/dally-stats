"""
Django settings for mwm-db project. Development environment.
"""

from .base import *

DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8wrk=v=8u9m@!#vyyej0#t2xblts&g$_g84(zmg0$t(5@je#01'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dally_stats',
        'USER': 'eyefox',
        'PASSWORD': '6obB[;Ln]Ea%-]$v8xujhSbAKBp<6L',
        'HOST': 'localhost',
        'PORT': '',
    }
}
