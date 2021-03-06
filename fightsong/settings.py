"""
Django settings for fightsong project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'fb107*ow@_gh*dfqj*fb6bio2q25=j_h_+kvjxqzid75i6!^@*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['fightsongdyno.herokuapp.com']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'round1',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'fightsong.urls'

WSGI_APPLICATION = 'fightsong.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
#
# DATABASES = {
#       'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'fightsong', # CREATE DATABASE heroku_example CHARACTER SET utf8 COLLATE utf8_general_ci;
#         'USER': 'root',
#         'PASSWORD': 'root',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
    }
}
# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'EST'
USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
MEDIA_ROOT = os.path.join(os.getcwd(),'media')#'C:/Users/Zachary/Desktop/Fall 2014/Advanced Software/cs3240project/media/'
MEDIA_URL = '/media/'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),

)
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'uvafightsong@gmail.com'
EMAIL_HOST_PASSWORD = 'alxsaddtuecclrks'

# # Allow all host hosts/domain names for this site
# ALLOWED_HOSTS = ['*']

# Parse database configuration from $DATABASE_URL
import dj_database_url

DATABASES['default'] = dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# try to load local_settings.py if it exists
try:
  from local_settings import *
except Exception as e:
  pass
