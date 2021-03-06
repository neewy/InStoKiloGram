"""
Django settings for InStoKiloGram project.

Generated by 'django-admin startproject' using Django 1.10.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

from .email_info import *
EMAIL_USE_TLS = EMAIL_USE_TLS
EMAIL_HOST = EMAIL_HOST
EMAIL_HOST_USER = EMAIL_HOST_USER
EMAIL_HOST_PASSWROD = EMAIL_HOST_PASSWROD
EMAIL_PORT = EMAIL_PORT
SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

import os
from DBSETTINGS import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'sy2w8hlq9)eysf6w9%yg4vqg3v7i4@_-xzp)lcp8%cw6@aic^@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'compressor',
    'Diets',
    'Recipes',
    'SocialNetwork',
    'SocialNetwork.Messages',
    'SocialNetwork.Wall',
    'Users',
    'Voting',
    'Blog',
    'Weight',
    'Food',
    'Exercises',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'InStoKiloGram.urls'

DOMAIN = 'http://dev.moo-moo.ru'

VK_REDIR = DOMAIN + '/vkoauthcb/'
VK_CLIENT_ID = 5649887
VK_CLIENT_SECRET ="SDICawCniimzVWAHGXhM"
VK_SCOPE = "profile,email"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),
                 os.path.join(BASE_DIR, 'InStoKiloGram/templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'InStoKiloGram.wsgi.application'

AUTH_USER_MODEL = 'Users.User'  # see http://stackoverflow.com/questions/30495979/django-1-8-multiple-custom-user-types

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = dbsettings()

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

# media dir
# http://zetblog.ru/programming/201303/django-static_root-staticfiles_dirs-media_root/

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'  # URL media

STATIC_ROOT = os.path.join(BASE_DIR, 'static')  # collectstatic

STATIC_URL = '/static/'  # URL static

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'assets'),
)

# Static files finder, first searches in STATICFILES_DIRS,

# second in the app's directories

STATICFILES_FINDERS = (

    'django.contrib.staticfiles.finders.FileSystemFinder',

    'django.contrib.staticfiles.finders.AppDirectoriesFinder',

    'compressor.finders.CompressorFinder',
)

COMPRESS_PRECOMPILERS = (
    ('text/less', 'lessc {infile} {outfile}'),
)

INTERNAL_IPS = ('127.0.0.1',)