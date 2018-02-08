from mywebsite.settings.common import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRESQL_DATABASE'),
        'USER': os.environ.get('POSTGRESQL_USER'),
        'PASSWORD': os.environ.get('POSTGRESQL_PASSWORD'),
        'HOST': os.environ.get('POSTGRESQL_HOSTS'),
        'PORT': '5432',
    }
}

MIDDLEWARE = MIDDLEWARE + ['whitenoise.middleware.WhiteNoiseMiddleware', ]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

INTERNAL_IPS = []