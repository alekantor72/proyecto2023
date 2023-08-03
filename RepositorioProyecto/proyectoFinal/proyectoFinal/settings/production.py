from .base import *

DEBUG = False

ALLOWED_HOSTS = ['alekantor72.pythonanywhere.com']
if not DEBUG:
    STATTIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'alekantor72$default',
        'USER': 'alekantor72',
        'PASSWORD': 'ranakantor1991',
        'HOST': 'alekantor72.mysql.pythonanywhere-services.com',
    }
}
