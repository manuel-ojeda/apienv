from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'LOLApi',
        'USER': 'lolapi_admin',
        'PASSWORD': '12345678',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}


STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]

MEDIA_ROOT = os.path.join(os.getcwd(), 'static/')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/