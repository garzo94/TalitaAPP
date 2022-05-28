from .base import *

SECRET_KEY = 'django-insecure-ul*@4nj)s!q#z=2da5u$024o1vly@n3&7=l2jg*@eadkq#y*vm'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

STATIC_URL = 'static/'

STATIC_ROOT =  BASE_DIR / 'staticfiles'

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR/'media'