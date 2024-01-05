"""
Django settings for architecture_archaeology project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

from dotenv import load_dotenv
from os import path, environ


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


load_dotenv(path.join(BASE_DIR.parent.absolute(), '.env'))

PROJECT = 'architecture_archaeology'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'testserver']

# Application definition

INSTALLED_APPS = [
    'arch_site.apps.ArchSiteConfig',
    'artefact.apps.ArtefactConfig',
    'helpers.apps.HelpersConfig',
    'building.apps.BuildingConfig',
    'index.apps.IndexConfig',
    'artwork.apps.ArtworkConfig',
    'file.apps.FileConfig',
    "debug_toolbar",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = 'architecture_archaeology.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries': {'settings_value': 'helpers.templatetags.settings_value'}
        },
    },
]

WSGI_APPLICATION = 'architecture_archaeology.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'aa_db',
        'HOST': '158.160.98.190',
        'USER': 'test',
        'PASSWORD': 'test',
        'PORT': '55432',
        'ATOMIC_REQUESTS': True,
        "TEST": {
            "NAME": "aa-testdb",
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

INTERNAL_IPS = [
    "127.0.0.1",
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

# DATA_UPLOAD_MAX_NUMBER_FILES = 2

USE_I18N = True

USE_TZ = True

GMAPS_API_KEY = 'AIzaSyDv88hb7YC6T0VfFMj6AprpmP4Vfut1GTs'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{name}:{levelname}:{asctime}:{funcName}:{message}",
            "datefmt": '%Y-%m-%d %H-%M-%S',
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
    },
    "filters": {
        # "special": {
        #     "()": "project.logging.SpecialFilter",
        #     "foo": "bar",
        # },
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "simple": {
            "level": "INFO",
            "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        # "mail_admins": {
        #     "level": "ERROR",
        #     "class": "django.utils.log.AdminEmailHandler",
        #     "filters": ["special"],
        # },
    },
    "loggers": {
        "django": {
            "handlers": ["simple"],
            "propagate": True,
        },
        # "django.server": {
        #     "handlers": ["console_simple"],
        #     "level": "INFO",
        #     "propagate": False,
        # },
        PROJECT: {
            "handlers": ["console"],
            "level": "INFO"
        },
    },
}

# Yandex cloud S3 config params

OBJECT_STORAGE_URL = environ.get('OBJECT_STORAGE_URL')

BUCKET = environ.get('BUCKET')

AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')

AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')
