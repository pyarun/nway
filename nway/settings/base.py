"""
Django settings for nway project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.core.urlresolvers import reverse_lazy
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

PROJECT_PATH = os.path.split(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))[0]
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f7$s94p0=s&-=)@787_1%f-wdr2l4$7$_)f(3=vvp!9h%co#dy'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'south',
    'compressor',
    'django_extensions',
    "categories.editor",
    "photologue",
    'seo',
    'taggit',
    'rest_framework',
    'registration',
    'django_js_reverse'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

AUTHENTICATION_BACKENDS = ('main.backends.EmailAuthBackend',)

ROOT_URLCONF = 'nway.urls'

WSGI_APPLICATION = 'nway.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_ROOT = os.path.join(PROJECT_PATH, "assets")

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.abspath(os.path.join(PROJECT_PATH, "static")),
)

SOUTH_MIGRATION_MODULES = {
    'taggit': 'taggit.south_migrations',
}

ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window; you may, of course, use a different value.


LOGIN_URL = reverse_lazy("nway_login")