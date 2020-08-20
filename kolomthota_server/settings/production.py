from .base import *

SECRET_KEY = get_config('SECRET_KEY')

DEBUG = False

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

if get_config('IS_AUTHENTICATION_ENABLED') == "False":
    REST_FRAMEWORK['DEFAULT_PERMISSION_CLASSES'] = ()
