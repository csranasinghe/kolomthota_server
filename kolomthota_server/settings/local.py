from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = get_config('ALLOWED_HOSTS')

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_config('DB_NAME'),
        'USER': get_config('DB_USER'),
        'PASSWORD': get_config('DB_PASSWORD'),
        'HOST': get_config('DB_HOST'),
        'PORT': get_config('DB_PORT')
    }
}