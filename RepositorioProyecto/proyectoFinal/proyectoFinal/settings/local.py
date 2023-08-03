from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['alekantor72.pythonanywhere.com']

if not DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

#ESTA ES LA CONFIGURACION PARA BD SQLITE
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'proyecto2023',
        'USER': 'root',
        'PASSWORD': 'ranakantor1991',
        'HOST': 'localhost',
    }
}
